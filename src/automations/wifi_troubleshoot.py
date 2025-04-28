import psutil
from typing import List, Dict

def get_wifi_troubleshooting_steps() -> List[Dict[str, str]]:
    """Returns step-by-step WiFi troubleshooting guides"""
    return [
        {
            "title": "🔌 Basic Checks",
            "steps": [
                "1. Check if WiFi is enabled on your device",
                "2. Verify airplane mode is OFF",
                "3. Restart your router (unplug for 30 seconds)"
            ]
        },
        {
            "title": "📶 Advanced Fixes",
            "steps": [
                "1. Forget network and reconnect",
                "2. Update network drivers",
                "3. Run network diagnostics (Windows: `netsh winsock reset`)"
            ]
        }
    ]

def check_wifi_connection() -> bool:
    """Check if system has active WiFi connection"""
    try:
        interfaces = psutil.net_if_stats()
        return any(
            iface.isup and "wi-fi" in name.lower()
            for name, iface in interfaces.items()
        )
    except:
        return False

def generate_wifi_report() -> str:
    """Generate a formatted WiFi status report"""
    is_connected = check_wifi_connection()
    status = "✅ Connected" if is_connected else "❌ Disconnected"
    
    report = [
        f"### WiFi Status: {status}",
        "### Troubleshooting Guides:"
    ]
    
    for section in get_wifi_troubleshooting_steps():
        report.append(f"\n**{section['title']}**")
        report.extend(section['steps'])
    
    return "\n".join(report)