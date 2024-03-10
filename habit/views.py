from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from habit.models import Habit
from habit.paginators import HabitPaginator
from habit.serializers import HabitSerializer
from habit.permissions import IsOwnerOrReadOnly


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]  # Добавляем кастомное разрешение
    pagination_class = HabitPaginator

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Указываем текущего пользователя как владельца привычки
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
