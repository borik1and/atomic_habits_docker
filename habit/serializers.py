from rest_framework import serializers

from habit.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, attrs):
        related_habit = attrs.get('related_habit')
        reward = attrs.get('reward')

        if related_habit and reward:
            raise serializers.ValidationError(
                "Нельзя одновременно выбрать связанную привычку и указать вознаграждение.")

        return attrs
