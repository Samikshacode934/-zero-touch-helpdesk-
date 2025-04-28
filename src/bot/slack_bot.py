import os
import sys
import logging
from pathlib import Path
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from prometheus_client import start_http_server, Counter

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

# ================== COMMAND HANDLERS ==================

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

# ================== ACTION HANDLERS ==================

@app.action("password_reset")
def handle_password_reset(ack, body, respond):
    """Handle password reset requests"""
    ack()
    try:
        # Get user email from Slack payload
        user_email = body["user"].get("email", "user@example.com")
        
        # Generate password (mock implementation)
        temp_pw = f"Temp{os.urandom(2).hex()}!" 
        
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

# ================== BOT STARTUP ==================

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