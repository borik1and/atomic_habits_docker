from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response

from habit.models import Habit
from habit.paginators import HabitPaginator
from habit.serializers import HabitSerializer
from users.services import TelegramBotService


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPaginator

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def send_telegram_message(request):
    chat_id = request.data.get('chat_id')
    text = request.data.get('text')
    if not chat_id or not text:
        return Response({'error': 'Missing chat_id or text'}, status=400)

    telegram_service = TelegramBotService()
    response = telegram_service.send_message(chat_id, text)

    if response.status_code == 200:
        return Response({'message': 'Message sent successfully'}, status=200)
    else:
        return Response({'error': 'Failed to send message'}, status=500)
