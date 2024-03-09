from rest_framework.routers import DefaultRouter
from django.urls import path
from habit.views import HabitViewSet, send_telegram_message

app_name = 'habit'

router = DefaultRouter()
router.register(r'habit', HabitViewSet, basename='habit')

urlpatterns = [
    path('send-telegram-message/', send_telegram_message, name='send-telegram-message'),
              ] + router.urls
