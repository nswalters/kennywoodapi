import json
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from kennywoodapi.models import Visitor
from rest_framework.authtoken.models import Token


class UserTests(APITestCase):
    def setUp(self) -> None:
        pass

    def test_register_new_user(self):
        """
        Ensure we can register a new user
        """

        url = "/register"
        data = {
            "username": "test@test.com",
            "email": "test@test.com",
            "password": "password",
            "first_name": "test_firstname",
            "last_name": "test_lastname",
            "phone_number": "123-456-7890",
            "special_requirements": "wheelchair",
            "number_family_members": 3
        }
        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("token", json_response)

    def test_successful_login_user(self):
        """
        Ensure that we can login with a registered user
        """

        # Make sure we have a registered user
        self.test_register_new_user()

        url = "/login"
        data = {
            "username": "test@test.com",
            "password": "password"
        }
        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response["valid"], True)
        self.assertIn("token", json_response)

    def test_unsuccessful_login_user_bad_username(self):
        """
        Ensure that bad credentials are not accepted
        """

        # Make sure we have a registered user
        self.test_register_new_user()

        url = "/login"

        # First test bad username
        data = {
            "username": "idontexist",
            "password": "password"
        }
        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(json_response["valid"], False)

    def test_unsuccessful_login_user_bad_password(self):

        # Make sure we have a registered user
        self.test_register_new_user()

        url = "/login"

        # Next test bad password
        data = {
            "username": "test@test.com",
            "password": "badpassword"
        }

        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(json_response["valid"], False)
