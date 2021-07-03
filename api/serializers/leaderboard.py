from rest_framework import serializers

from api.serializers import EventSerializer
from course.models.models import LeaderBoard

class LeaderBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaderBoard
        fields = ['name', 'course','created_by']
