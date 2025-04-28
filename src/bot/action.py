from slack_bolt import Ack

def handle_password_reset(ack: Ack, body: dict, client):
    ack()
    client.chat_postMessage(
        channel=body["user"]["id"],
        text="Your temporary password: Temp123! (Mock)"
    )

def handle_wifi_help(ack: Ack, body: dict, client):
    ack()
    client.chat_postMessage(
        channel=body["user"]["id"],
        text="Try these steps:\n1. Restart router\n2. Reconnect to 'CompanyWiFi'"
    )