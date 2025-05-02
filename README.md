🔧 Zero-Touch Helpdesk Bot for Slack 🤖
Automating IT support. Saving time. Empowering teams.

🧠 Overview:-
👉Zero-Touch Helpdesk is an intelligent Slack bot designed to automate 40%+ of repetitive IT helpdesk tickets — such as password resets and WiFi troubleshooting — through real-time Slack interactions.
Built in just weeks as part of the Agentforce Hackathon, this project showcases how AI and automation can streamline enterprise operations, reduce response time, and give IT teams their time back.

🚀 Key Features
🔐 Instant Password Reset
Generates secure, temporary credentials for users in seconds. | ✅ Working |

📶 WiFi Troubleshooting Assistant
Guides users through common connectivity issues automatically.| ✅ Working |

| 🧠 AI Ticket Classification and openai for language model integration| GPT-3.5 powered ticket        categorization | 🚧  MVP(in progress) |
  Respond to /ticket commands and shortcuts with intractive modals and buttons.

📡 Real-time Slack Integration
Responds to /helpdesk commands and shortcuts with interactive modals and buttons.

⚙️ Salesforce Ticket Generation 🚧 (in planed)
Automatically logs interactions to Salesforce for auditing and compliance.

🔒 Security Focused
👉OAuth 2.0 for Slack + Salesforce
👉No data persistence
👉All actions logged for traceability


🛠️Tech Stack:-
👉Component	Technology Used:-
🔥 Backend: Python + (Slack Bolt)
 **AI**: OpenAI GPT-3.5-turbo
- **Metrics**: Prometheus + Grafana
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
|   |   |__ disk_alert.py
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
|   |__ test_wifi.py       # Test cases
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
|── README.md            # Project overviewing deepseek_bash_20250424_f051ea (1).sh…]()
|__ setup.py
|__ ticket.csv


⚡ Quick Start
1. Prerequisites
Python 3.8+
🔥Slack workspace (admin permission  (https://app.slack.com/client/T08MB5YCYPR/D08MBLJ6XAT))

🧪 Project Status:-
✅ Core logic complete
✅ Slack actions (password reset, WiFi help) live
✅ Working Slack bot via Socket Mode

⚙️ Salesforce integration and dashboard still in progress



📦 Getting Started
Installation:-
1. Clone the repo
git clone https://github.com/Samikshacode934/-zero-touch-helpdesk-.git
cd -zero-touch-helpdesk-
pip install -r requirements.txt


2. Create your .env file
Configuration:-
Copy .env.example to .env and fill in:
SLACK_BOT_TOKEN=xoxb-...
SLACK_APP_TOKEN=xapp-1-...


🤖3. Run the bot
  python src/bot/slack_bot.py

You should see⬇️
⚡️ Bolt app is running!


flowchart TD
    A[Slack Command] --> B[Python Bot]
    B --> C[Password Reset/Wi-Fi Automation]
    C --> E[AI Classifier]
    D --> D[Log to CSV/Sheets]
    E --> E[Streamlit Dashboard]
