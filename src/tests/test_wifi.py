from src.automations.wifi_troubleshoot import (
    get_wifi_troubleshooting_steps,
    check_wifi_connection,
    generate_wifi_report
)

def test_troubleshooting_steps():
    steps = get_wifi_troubleshooting_steps()
    assert len(steps) >= 2
    assert "Basic Checks" in steps[0]["title"]

def test_report_generation():
    report = generate_wifi_report()
    assert "WiFi Status" in report
    assert "Troubleshooting Guides" in report