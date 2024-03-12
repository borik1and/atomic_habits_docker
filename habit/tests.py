from rest_framework_simplejwt.tokens import AccessToken
from users.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from habit.models import Habit


class HabitViewSetTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password', is_active=True)
        self.client.force_authenticate(user=self.user)
        self.token = AccessToken.for_user(self.user)  # Создаем токен для пользователя

    def test_create_habit(self):
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + str(self.token))  # Устанавливаем токен в заголовке запроса
        url = reverse('habit:habit-list')
        data = {
            "name": "test11",
            "action": "test1",
            "place": "test",
            "period": 1,
            "reward": "test",
            "user": 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 1)
        self.assertEqual(Habit.objects.get().name, 'test11')

    def test_retrieve_habit(self):
        habit = Habit.objects.create(
            user=self.user,
            name='Test Habit',
            action='Test Action',
            place='Test Place',
            sign_pleasant_habit=False,
            period='3',
            reward='',
            time_to_complete='00:01:00',
            is_public=False
        )
        url = reverse('habit:habit-detail', kwargs={'pk': habit.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Habit')

    def test_update_habit(self):
        habit = Habit.objects.create(
            user=self.user,
            name='Test Habit',
            action='Test Action',
            place='Test Place',
            sign_pleasant_habit=False,
            period='1',
            reward='',
            time_to_complete='00:01:00',
            is_public=False
        )
        url = reverse('habit:habit-detail', kwargs={'pk': habit.id})
        data = {'name': 'Updated Habit'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Habit')

    def test_delete_habit(self):
        habit = Habit.objects.create(
            user=self.user,
            name='Test Habit',
            action='Test Action',
            place='Test Place',
            sign_pleasant_habit=False,
            period='1',
            reward='',
            time_to_complete='00:01:00',
            is_public=False
        )
        url = reverse('habit:habit-detail', kwargs={'pk': habit.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 0)
