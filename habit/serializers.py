from rest_framework import serializers
from datetime import timedelta
from habit.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

    def validate_related_habit(self, value):
        if value and not value.sign_pleasant_habit:
            raise serializers.ValidationError(
                "Связанная привычка должна быть приятной."
            )
        return value

    def validate_reward(self, value):
        if self.instance and self.instance.sign_pleasant_habit and value:
            raise serializers.ValidationError(
                "При приятной привычке нельзя указывать вознаграждение."
            )
        return value

    def validate(self, attrs):
        related_habit = attrs.get('related_habit')
        reward = attrs.get('reward')
        time_to_complete = attrs.get('time_to_complete')
        period = attrs.get('period')

        if related_habit and reward:
            raise serializers.ValidationError(
                "Нельзя одновременно выбрать связанную привычку"
                " и указать вознаграждение."
            )

        if time_to_complete and time_to_complete > timedelta(minutes=2):
            raise serializers.ValidationError(
                "Нельзя выполнять привычку более 2х минут."
            )

        if period and period > timedelta(days=7):
            raise serializers.ValidationError(
                "Нельзя устанавливать привычку реже, чем 1 раз в 7 дней."
            )

        return attrs
