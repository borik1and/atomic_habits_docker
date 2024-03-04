from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from habit.models import Habit
from habit.serializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
