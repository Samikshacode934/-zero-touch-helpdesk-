import pytest
import sys
from pathlib import Path

# Fix 1: Correct path modification (use insert instead of append)
sys.path.insert(0, str(Path(__file__).parent.parent))

# Fix 2: Verify the path exists
try:
    from src.automations.password_reset import generate_temp_password
except ImportError as e:
    print(f"Import failed. Python path: {sys.path}")
    raise

def test_password_generation():
    """Test temp password meets security requirements"""
    test_email = "test@example.com"
    pw = generate_temp_password(test_email)
    
    # Length check
    assert len(pw) >= 8, "Password too short"
    
    # Complexity checks
    assert any(c.isupper() for c in pw), "Missing uppercase"
    assert any(c.isdigit() for c in pw), "Missing digit"
    assert any(not c.isalnum() for c in pw), "Missing special char"

@pytest.mark.parametrize("email", [
    "user1@company.com",
    "admin@org.gov",
    "test+alias@domain.net"
])
def test_multiple_emails(email):
    pw = generate_temp_password(email)
    assert len(pw) >= 8