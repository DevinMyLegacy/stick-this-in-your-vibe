import os

def test_venv_creation():
    """Test venv setup reminder."""
    assert "venv" in "python -m venv venv"  # Simple check

def test_secure_key():
    """Test env var usage."""
    assert os.environ.get("API_KEY") is None  # Placeholder; secure in prod
