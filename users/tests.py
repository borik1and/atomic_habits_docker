from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User


class UserAPITest(APITestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'phone': '1234567890',
            'password': 'Test',

        }
        self.invalid_user_data = {
            'username': 'testuser2',

        }

    def test_user_registration(self):
        url = reverse('user:registration')
        response = self.client.post(url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_invalid_user_registration(self):
        url = reverse('user:registration')
        response = self.client.post(url, self.invalid_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_login(self):
        # Assuming you have implemented user login logic and have a URL for it
        url = reverse('user:login')
        response = self.client.post(url, {}, format='json')  # Pass any required login data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, "Аутентификация успешна")
