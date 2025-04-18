from rest_framework import serializers
from ..models import Task
from datetime import date

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate_title(self, value): #validate title
        if not value:
            raise serializers.ValidationError("Title is required.")
        return value

    def validate_due_date(self, value):  #validate due_date
        if value < date.today():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value
