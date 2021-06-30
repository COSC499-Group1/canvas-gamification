
from rest_framework import viewsets

from leader_board.models import LeaderBoardAssignedStudents
from api.serializers.leader_board import LeaderBoardSerializer

class LeaderBoardViewSet(viewsets.ModelViewSet):
    serializer_class = LeaderBoardSerializer
    filterset_fields = ['student','tokens','course' ]

    def get_queryset(self):
        # return MyUser.objects.all() #Use with actual users in database

        return LeaderBoard.objects.all()
    