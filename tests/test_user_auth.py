import pytest
import allure
import requests

class TestUserAuth():
    def setup(self):
        self.email = 'a.mosyakin@itdept.cloud'
        self.phone = '+79874121943'
        self.password = 'rewq4321'

    def test_auth_user_email(self):
        data_email = {
            'email': self.email,
            'password': self.password
        }

        response_email = requests.post('https://kazino-back-demo.dev2.itdept.cloud/api/v1/auth/login/', data=data_email)

        result_body = response_email.json()

        expected_email = self.email
        result_email = result_body['user']['email']

        assert expected_email == result_email, f'Expected email {expected_email} not equal result email {result_email}'
