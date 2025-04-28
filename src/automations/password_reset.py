import random
import string
from datetime import datetime
import csv
from pathlib import Path

def generate_temp_password(email):
    """Generate secure temporary password"""
    special_chars = "!@#$%^&*"
    password = [
        random.choice(string.ascii_uppercase),  # At least 1 uppercase
        random.choice(string.digits),           # At least 1 digit
        random.choice(special_chars)            # At least 1 special char
    ]
    # Add random characters to reach length
    password += random.choices(
        string.ascii_letters + string.digits + special_chars,
        k=random.randint(5, 10)  # Random length between 8-13 chars
    )
    random.shuffle(password)
    
    temp_pw = "".join(password)
    log_reset(email, temp_pw)
    return temp_pw

def log_reset(email, password):
    """Log resets to CSV with headers if file doesn't exist"""
    log_file = Path(__file__).parent.parent / "password_reset_logs.csv"
    
    # Create file with headers if it doesn't exist
    if not log_file.exists():
        with open(log_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "email", "temp_password"])
    
    # Append new entry
    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().isoformat(timespec='seconds'),  # Cleaner timestamp
            email,
            password
        ])

# Test function (optional)
if __name__ == "__main__":
    # Generate 5 test entries when run directly
    for i in range(5):
        print(f"Test {i+1}:", generate_temp_password(f"test{i}@example.com"))
    print("Data logged to:", Path(__file__).parent.parent / "password_reset_logs.csv")