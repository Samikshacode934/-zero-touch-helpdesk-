Zero-Touch IT Helpdesk Bot 🤖
*A Slack bot that automates 40% of repetitive IT tickets (password resets, Wi-Fi troubleshooting, and proactive alerts)



🚀 Features
/helpdesk command: Instant IT support via Slack.

One-click fixes:

🔑 Auto-generate temporary passwords.

📶 Wi-Fi troubleshooting guides.

Proactive alerts: Disk space warnings, system health checks.

Admin dashboard: Streamlit analytics for ticket tracking.



🛠️ Technical Architecture
zero-touch-helpdesk/
├── .github/                  # GitHub configs
│   └── workflows/
│       └── test.yml          # CI/CD pipeline
├── .vscode/                 # IDE settings (optional)
├── docs/                    # Documentation (MkDocs/Sphinx)
├── src/
│   ├── automations/         # Core logic
│   │   ├── __init__.py
│   │   ├── password_reset.py
│   │   └── wifi_troubleshoot.py
│   ├── bot/                # Slack bot
│   │   ├── __init__.py
│   │   ├── slack_bot.py    # Main bot
│   │   ├── actions.py      # Button handlers
│   │   └── server.py       # Flask/SocketMode
│   └── dashboard.py        # Streamlit analytics
├── tests/                  # Unit tests
│   ├── __init__.py
│   ├── conftest.py        # Pytest fixtures
│   └── test_bot.py        # Test cases
├── website/               # Web UI (optional)
│   ├── static/
│   │   └── style.css
│   ├── templates/
│   │   ├── index.html
│   │   └── dashboard_frame.html
│   └── app.py             # Flask server
├── .env.example           # Template for env vars
├── .gitignore            # Ignores .env, __pycache__
├── Dockerfile            # Containerization
├── LICENSE
├── pytest.ini            # Pytest config
├── requirements.txt      # Dependencies
└── README.md            # Project overview


Tech Stack
Component	Technology Used
Backend	Python (Slack Bolt)
Data Storage	Google Sheets (or CSV)
Dashboard	Streamlit
Hosting	GitHub Codespaces (Dev) 


⚡ Quick Start
1. Prerequisites
Python 3.8+

Slack workspace (admin permission  (https://app.slack.com/client/T08MB5YCYPR/D08MBLJ6XAT))


2. Setup
3. # Clone repo
git clone https://github.com/Samikshacode934/-zero-touch-helpdesk-.git
cd -zero-touch-helpdesk-

# Install dependencies
pip install -r requirements.txt

# Add Slack tokens to .env
echo "SLACK_BOT_TOKEN=xoxb-BOT-token" > .env
echo "SLACK_APP_TOKEN=xapp-APP-token" >> .env


3. Run the Bot
4. python src/bot/slack_bot.py

   4. Access Dashboard
   5. streamlit run src/dashboard.py
  

  🙋 FAQ
Q: How do I test the bot?
A: Type /helpdesk in any Slack channel after running slack_bot.py.

Q: Where’s the demo video?
A: Watch here. (Add your YouTube link)


flowchart TD
    A[Slack Command] --> B[Bot Server]
    B --> C[Password Reset/Wi-Fi Automation]
    C --> D[Log to CSV/Sheets]
    D --> E[Streamlit Dashboard]
