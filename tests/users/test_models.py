"""
-------------------
Tetsting User Model
-------------------
"""
import pytest


def test_user_str(base_user):
    """Tets the custom user model string representation"""
    assert base_user.__str__() == base_user.username


def test_user_short_name(base_user):
    """Test that user model get_short_name method work"""
    short_name = f"{base_user.username}"
    assert base_user.get_short_name == short_name


def test_user_full_name(base_user):
    """Test that user model full_name method work"""
    full_name = f"{base_user.first_name} {base_user.last_name}"
    assert base_user.full_name == full_name


def test_base_user_email_is_normalized(base_user):
    """Test that the email for a new user is normalized"""
    email = "alpha@REALEsTATE.COM"
    assert base_user.email == email.lower()


def test_super_user_email_is_normalized(super_user):
    """Test that the email for a new user is normalized"""
    email = "alpha@REALEsTATE.COM"
    assert super_user.email == email.lower()


def test_super_user_is_not_staff(user_factory):
    """Test that an errror is raised when a superuser is not staff set to false"""
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=True, is_staff=False)
    assert str(err.value) == "Superuser must have is_staff=True."


def test_super_user_is_not_superuser(user_factory):
    """Test that an errror is raised when an admin has is_superuser set to false"""
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=False, is_staff=True)
    assert str(err.value) == "Superuser must have is_superuser=True."


def test_create_user_with_no_email(user_factory):
    """Test that an error is raised when a user is created with no email"""
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None)
    assert str(err.value) == "Base User Account: An email address is required"


def test_create_user_with_no_username(user_factory):
    """Test that an error is raised when a user is created with no username"""
    with pytest.raises(ValueError) as err:
        user_factory.create(username=None)
    assert str(err.value) == "User must submit a username"


def test_create_user_with_no_firstname(user_factory):
    """Test that an error is raised when a user is created with no first_name"""
    with pytest.raises(ValueError) as err:
        user_factory.create(first_name=None)
    assert str(err.value) == "User must submit a first name"


def test_create_user_with_no_lastname(user_factory):
    """Test that an error is raised when a user is created with no last_name"""
    with pytest.raises(ValueError) as err:
        user_factory.create(last_name=None)
    assert str(err.value) == "User must submit a last name"


def test_create_user_with_no_valid_email(user_factory):
    """Test that an error is raised when a user is created with no valid email"""
    with pytest.raises(ValueError) as err:
        user_factory.create(email="This is not a valid email")
    assert str(err.value) == "You must provide a valid email address"


def test_create_superuser_with_no_email(user_factory):
    """Test that an error is raised when a superuser is created with no email"""
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None, is_superuser=True, is_staff=True)
    assert str(err.value) == "Admin Account: An email address is required"


def test_create_superuser_with_no_password(user_factory):
    """Test that an error is raised when a superuser is created with no password"""
    with pytest.raises(ValueError) as err:
        user_factory.create(password=None, is_superuser=True, is_staff=True)
    assert str(err.value) == "Superuser must submit a password"
