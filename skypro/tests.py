from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User(email='ayta@sky.pro')
        self.user.set_password('123random_password456')
        self.user.save()

        response = self.client.post(
            '/api/token/',
            {'email': 'ayta@sky.pro', 'password': '123random_password456'}
        )

        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTORIZATION=f'Bearer {self.access_token}')
        self.client.force_authenticate(user=self.user)

    def test_lesson_list(self):
        self.test_lesson_create()
        response = self.client.get('/skypro/lesson/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_create(self):
        response = self.client.post("/skypro/lesson/create/", {
            "title": "OOP",
            "link_video": "https: // www.youtube.com"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_lesson_update(self):
        self.test_lesson_create()
        response = self.client.put("/skypro/lesson/update/1/", {
            "title": "OOP",
            "link_video": "https: // www.youtube.com"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_detail(self):
        self.test_lesson_create()
        response = self.client.get('/skypro/lesson/retrieve/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_delete(self):
        self.test_lesson_create()
        response = self.client.delete('/skypro/lesson/destroy/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SubscriptionTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User(email='ayta_2@sky.pro')
        self.user.set_password('123random_password456')
        self.user.save()

        response = self.client.post(
            '/api/token/',
            {'email': 'ayta@sky.pro', 'password': '123random_password456'}
        )

        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTORIZATION=f'Bearer {self.access_token}')
        self.client.force_authenticate(user=self.user)

    def test_subscription_create(self):
        response = self.client.post('/skypro/subscription/create/', {'course_id_id': 1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_subscription_update(self):
        self.test_subscription_create()
        response = self.client.put("/skypro/subscription/update/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
