from rest_framework import serializers

from api.serializers import EventSerializer
from course.models.models import LeaderBoardStudents

class LeaderBoardStudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaderBoardStudents
        fields = ['student', 'course', 'leader_board', 'token_value', 'team', 'streak']
