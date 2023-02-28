from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User(email="ayta@sky.pro")
        self.user.set_password("random_password")
        self.user.save()

        response = self.client.post("/users/api/token/", {"email": "ayta@sky.pro", "password": "random_password"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTORIZATION=f"Bearer {self.access_token}")
        self.client.force_authenticate(user=self.user)

    def test_lesson_create(self):
        response = self.client.post("/skypro/lesson/create/", {
            "title": "OOP",
            "link_video": "https: // www.youtube.com"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expected_data = {'title': 'OOP', 'image': None, 'description': None, "link_video": "https: // www.youtube.com"}
        self.assertEqual(response.json(), expected_data)

    def test_lesson_update(self):
        self.test_lesson_create()
        response = self.client.put("/skypro/lesson/update/2/", {
            "title": "OOP",
            "link_video": "https: // www.youtube.com"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = {"title": "OOP", "image": None, "description": None, "link_video": "https: // www.youtube.com"}
        self.assertEqual(response.json(), expected_data)

    def test_lesson_list(self):
        self.test_lesson_create()
        response = self.client.get('/skypro/lesson/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = [
            {"title": "OOP", "image": None, "description": None, "link_video": "https: // www.youtube.com"}]
        self.assertEqual(response.json(), expected_data)

    def test_lesson_delete(self):
        self.test_lesson_create()
        response = self.client.delete('/skypro/destroy_lesson/2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_lesson_detail(self):
        self.test_lesson_create()
        response = self.client.get('/skypro/retrieve_lesson/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = {"title": "new", "image": None, "description": None, "link_video": "https: // www.youtube.com"}
        self.assertEqual(response.json(), expected_data)


class SubscriptionTestCase(APITestCase):
    def setUp(self) -> None:
        super().setUp()
        self.user = User(email="ayta@sky.pro")
        self.user.set_password("random_password")
        self.user.save()

        response = self.client.post("/users/api/token/", {"email": "ayta@sky.pro", "password": "random_password"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTORIZATION=f"Bearer {self.access_token}")
        self.client.force_authenticate(user=self.user)

    def test_subscription_create(self):
        response = self.client.post("/training/subscription/create/", {"course_id": 1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expected_data = {
            "id": 1,
            "status": "active",
            "course_id": 1
        }
        self.assertEqual(response.json(), expected_data)

    def test_subscription_delete(self):
        self.test_subscription_create()
        response = self.client.put("/skypro/subscription/delete/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = {
            "id": 1,
            "status": "inactive",
            "course_id": 1
        }
