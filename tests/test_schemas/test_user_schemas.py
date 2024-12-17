from app.schemas.user_schemas import UserBase, UserCreate, UserUpdate, UserResponse
import pytest

def test_user_base_valid():
    """
    Test the UserBase schema with valid input.
    """
    user = UserBase(
        name="John Doe", 
        email="john.doe@example.com", 
        nickname="johndoe", 
        profile_pic_url="http://example.com/profile.jpg"
    )
    assert user.name == "John Doe"
    assert user.email == "john.doe@example.com"
    assert user.nickname == "johndoe"
    assert user.profile_pic_url == "http://example.com/profile.jpg"

def test_user_create_valid():
    """
    Test the UserCreate schema with valid input.
    """
    user = UserCreate(
        name="John Doe", 
        email="john.doe@example.com", 
        password="strongpassword123", 
        nickname="johndoe"
    )
    assert user.password == "strongpassword123"
    assert user.email == "john.doe@example.com"

def test_user_update_valid():
    """
    Test the UserUpdate schema with partial updates.
    """
    user_update = UserUpdate(name="Updated Name", email="updated@example.com")
    assert user_update.name == "Updated Name"
    assert user_update.email == "updated@example.com"

def test_user_response_valid():
    """
    Test the UserResponse schema with full input.
    """
    user_response = UserResponse(
        id=1,
        name="John Doe",
        email="john.doe@example.com",
        nickname="johndoe",
        profile_pic_url="http://example.com/profile.jpg"
    )
    assert user_response.id == 1
    assert user_response.name == "John Doe"
    assert user_response.email == "john.doe@example.com"
    assert user_response.nickname == "johndoe"
    assert user_response.profile_pic_url == "http://example.com/profile.jpg"

def test_user_update_partial():
    """
    Test UserUpdate schema with only nickname.
    """
    user_update = UserUpdate(nickname="newnickname")
    assert user_update.nickname == "newnickname"
