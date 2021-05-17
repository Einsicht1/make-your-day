from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "test@einsicht.com"
        password = 'unsafepass111'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_eamil_normalized(self):
        """Test the email for a new user is normalized"""
        email = "test@EINSICHT.COM"
        user = get_user_model().objects.create_user(email, 'testtest111')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        # ValueError를 일으켜야 테스트가 통과됨
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            "test@einsicht.com",
            'test1212'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
