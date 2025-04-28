import os
from dotenv import load_dotenv
from flask import Flask, request
from slack_bolt import App
from pathlib import Path
# Replace your Flask initialization with:
flask_app = Flask(__name__)

@flask_app.before_request
def verify_slack_request():
    """Verify Slack signing secret for all requests"""
    if request.path == "/slack/events":
        from slack_bolt.adapter.flask import SlackRequestHandler
        SlackRequestHandler.verify_signature(
            signing_secret=os.environ["SLACK_SIGNING_SECRET"],
            body=request.get_data(),
            headers=request.headers
        )


# Load environment from .env in parent directory
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(env_path)

# Debug print
print("Current working directory:", os.getcwd())
print("Environment variables:", {
    k: v[:3]+"..." if v and k in ['SLACK_BOT_TOKEN', 'SLACK_APP_TOKEN', 'SLACK_SIGNING_SECRET'] 
else v 
    for k, v in os.environ.items() 
    if 'SLACK' in k
    })

# Load environment variables
load_dotenv('/workspaces/-zero-touch-helpdesk-/.env')  

# Verify tokens exist
required_tokens = ['SLACK_BOT_TOKEN', 'SLACK_APP_TOKEN', 'SLACK_SIGNING_SECRET']
missing_tokens = [t for t in required_tokens if t not in os.environ]

if missing_tokens:
    print(f"CRITICAL: Missing environment variables: {missing_tokens}")
    print("Available variables:", [k for k in os.environ if "SLACK" in k])
    raise ValueError(
        f"Missing required Slack tokens: {', '.join(missing_tokens)}. "
        "Please ensure these tokens are set in your .env file or environment variables."
    )

# Initialize Slack app
slack_app = App(
    token=os.environ["SLACK_BOT_TOKEN"],
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET", "")
)

# Initialize Flask
flask_app = Flask(__name__)

@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return slack_app.handle(request)

if __name__ == "__main__":
    flask_app.run(port=3000, host="0.0.0.0")  