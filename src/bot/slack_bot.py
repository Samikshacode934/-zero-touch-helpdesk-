import os
import sys
import logging
from pathlib import Path
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from prometheus_client import start_http_server, Counter
import json  # Added for JSON handling
import requests  # Added for HTTP requests to LLM API
from openai import OpenAI  # Import or define your LLM client class here
class LLM:
    def __init__(self, model):
        self.model = model
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
def get_llm_client():
    return LLM(model="gpt-3.5-turbo")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add project root to Python path
root_path = str(Path(__file__).parent.parent)
src_path = str(Path(__file__).parent.parent / "src")
if root_path not in sys.path:
    sys.path.insert(0, root_path)
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# Load environment
env_path = Path(__file__).parent.parent.parent / '.env'
load_dotenv(env_path)

# Verify tokens
if not all(k in os.environ for k in ['SLACK_BOT_TOKEN', 'SLACK_APP_TOKEN']):
    raise ValueError("Missing Slack tokens in environment")

# Initialize app
app = App(token=os.environ["SLACK_BOT_TOKEN"])

# ================== LLM Functionality ==================

def classify_ticket(prompt, llm=None):
    """Use OpenAI to classify and generate ticket summary"""
    llm = llm or get_llm_client()
    system_prompt = (
        "You are an IT helpdesk assistant. Given a user issue, extract:\n"
        "- a short summary of the issue\n"
        "- the likely category (e.g. Network, Password, Hardware, Software)\n"
        "- a possible action the user can take now.\n"
        "Reply in JSON format:\n"
        '{"summary": "...", "category": "...", "suggested_action": "..."}'
    )

    
    try:
        response = llm.client.chat.completions.create(
            model=llm.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"LLM error: {e}"


# ================== Slack Commands and Handlers ==================

@app.command("/helpdesk")
def handle_helpdesk(ack, respond):
    """Main helpdesk command showing action buttons"""
    ack()
    try:
        respond(
            blocks=[
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": "🛠️ *Zero-Touch Helpdesk*"},
                },
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text": {"type": "plain_text", "text": "🔑 Reset Password"},
                            "action_id": "password_reset",
                            "style": "primary"
                        },
                        {
                            "type": "button",
                            "text": {"type": "plain_text", "text": "📶 WiFi Help"},
                            "action_id": "wifi_help"
                        }
                    ]
                }
            ]
        )
    except Exception as e:
        logger.error(f"Helpdesk command failed: {e}")

@app.command("/ticket")
def handle_ticket(ack, respond, command):
    """Handles ticket requests and classifies the issue"""
    ack()
    user_input = command.get("text", "").strip()
    if not user_input:
        respond("❗ Please describe your issue. Example: `/ticket My Outlook won't open.`")
        return

    # Call LLM to classify ticket and generate summary
    raw_response = classify_ticket(user_input)
    
    try:
        ticket = json.loads(raw_response)
    except json.JSONDecodeError:
        respond(f"⚠️ Couldn't parse AI output:\n```\n{raw_response}\n```")
        return

    # Send categorized ticket summary to the user
    respond(
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"📝 *Ticket Summary*\n• *Issue:* {ticket['summary']}\n• *Category:* {ticket['category']}\n• *Suggested Action:* {ticket['suggested_action']}"
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "✅ Yes"},
                        "action_id": "confirm_ticket"
                    },
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "❌ No"},
                        "action_id": "cancel_ticket"
                    }
                ]
            }
        ]
    )

@app.action("confirm_ticket")
def handle_confirm_ticket(ack, body, respond):
    """Confirm ticket creation"""
    ack()
    user = body["user"]["username"]
    respond(f"🎟️ Ticket has been created for <@{user}>. IT will review it shortly.")

@app.action("cancel_ticket")
def handle_cancel_ticket(ack, respond):
    """Cancel ticket creation"""
    ack()
    respond("🗑️ Ticket creation canceled.")

@app.action("password_reset")
def handle_password_reset(ack, body, respond):
    """Handle password reset requests"""
    ack()
    try:
        # Get user email from Slack payload
        user_email = body["user"].get("email", "user@example.com")
        # Generate password (mock implementation)
        temp_pw = f"Temp{os.urandom(2).hex()}!" 
      # Here you would call the actual password reset function from your system        
        respond(text=f"✅ Your temporary password: `{temp_pw}`\n*Expires in 1 hour*")
        logger.info(f"Password reset for {user_email}")
    except Exception as e:
        respond(text="❌ Failed to reset password. Please contact IT.")
        logger.error(f"Password reset error: {e}")

@app.action("wifi_help")
def handle_wifi_help(ack, body, respond):
    """Provide WiFi troubleshooting steps"""
    ack()
    try:
        respond(
            text=(
                "📶 *WiFi Troubleshooting*\n\n"
                "1. Restart your router\n"
                "2. Forget network and reconnect\n"
                "3. Check for system updates\n\n"
                "Still having issues? Contact IT."
            )
        )
    except Exception as e:
        logger.error(f"WiFi help failed: {e}")

# ================== Bot Startup ==================

if __name__ == "__main__":
    # Start metrics server
    start_http_server(8000)
    
    logger.info("Starting bot with Socket Mode...")
    try:
        handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
        handler.start()
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")
        sys.exit(1)
