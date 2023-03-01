from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User(email='12reqw@fsd.ru')
        self.user.set_password('123qwe456')
        self.user.save()

        response = self.client.post("/api/token/", {"email": "12reqw@fsd.ru", "password": "123qwe456"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTORIZATION=f"Bearer {self.access_token}")

    def test_create_user(self):
        response = self.client.post(path="/users/create_user/",
                                    data={"email": "oliya2023@test.ru", "password": "123qwe456"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
