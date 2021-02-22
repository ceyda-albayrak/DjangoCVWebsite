from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
class UserTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test", password="supersecretpassword",
        )
    def test_created_token_successfully(self):
        token = Token.objects.get(user=self.user)
        self.assertTrue(hasattr(self.user, "auth_token"))
