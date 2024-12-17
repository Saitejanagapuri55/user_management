from app.utils.security import hash_password, verify_password

def test_hash_password_with_valid_input():
    password = "securepassword"
    hashed = hash_password(password)
    assert verify_password(password, hashed)

def test_hash_password_fails_for_invalid_input():
    password = "securepassword"
    wrong_password = "wrongpassword"
    hashed = hash_password(password)
    assert not verify_password(wrong_password, hashed)
