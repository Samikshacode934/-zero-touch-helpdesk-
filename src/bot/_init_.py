from slack_bolt import App
app = App()

# Demo-friendly command: Shows instant value
@app.command("/fix")
def handle_fix(ack, respond):
    ack()
    respond("🔧 What should I auto-fix? \n1. Password \n2. WiFi \n3. Storage")