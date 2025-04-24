🔧 Zero-Touch Helpdesk Bot for Slack 🤖
Automating IT support. Saving time. Empowering teams.

🧠 Overview:-
👉Zero-Touch Helpdesk is an intelligent Slack bot designed to automate 40%+ of repetitive IT helpdesk tickets — such as password resets and WiFi troubleshooting — through real-time Slack interactions.
Built in just weeks as part of the Agentforce Hackathon, this project showcases how AI and automation can streamline enterprise operations, reduce response time, and give IT teams their time back.

🚀 Key Features
🔐 Instant Password Reset
Generates secure, temporary credentials for users in seconds.

📶 WiFi Troubleshooting Assistant
Guides users through common connectivity issues automatically.

📡 Real-time Slack Integration
Responds to /helpdesk commands and shortcuts with interactive modals and buttons.

⚙️ Salesforce Ticket Generation (in progress)
Automatically logs interactions to Salesforce for auditing and compliance.

🔒 Security Focused
👉OAuth 2.0 for Slack + Salesforce
👉No data persistence
👉All actions logged for traceability


🛠️Tech Stack:-
👉Component	Technology Used
🔥 Backend Python (Slack Bolt)
🔥 Data Storage Google Sheets (or CSV)
🔥 Dashboard Streamlit
🔥 Hosting	GitHub Codespaces (Dev) 
🔥 Python 3.11
🔥 Slack Bolt SDK
🔥 Socket Mode
🔥 Prometheus (metrics)
🔥 Dotenv (env config)
🔥 GitHub Actions (CI for testing)





🛠️ Technical Architecture
[Uploadzero-touch-helpdesk/
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
└── README.md            # Project overviewing deepseek_bash_20250424_f051ea (1).sh…]()



⚡ Quick Start
1. Prerequisites
Python 3.8+
🔥Slack workspace (admin permission  (https://app.slack.com/client/T08MB5YCYPR/D08MBLJ6XAT))

🧪 Project Status:-
✅ Core logic complete
✅ Slack actions (password reset, WiFi help) live
✅ Working Slack bot via Socket Mode
⚙️ Salesforce integration and dashboard still in progress

🖥️ Demo (Coming Soon)
Stay tuned for a full walkthrough video + demo screenshots.


📦 Getting Started
1. Clone the repo
git clone https://github.com/Samikshacode934/-zero-touch-helpdesk-.git
cd -zero-touch-helpdesk-


2. Create your .env file
Copy .env.example to .env and fill in:
SLACK_BOT_TOKEN=xoxb-...
SLACK_APP_TOKEN=xapp-1-...


🤖3. Run the bot
  python src/bot/slack_bot.py

You should see⬇️
⚡️ Bolt app is running!


flowchart TD
    A[Slack Command] --> B[Bot Server]
    B --> C[Password Reset/Wi-Fi Automation]
    C --> D[Log to CSV/Sheets]
    D --> E[Streamlit Dashboard]
