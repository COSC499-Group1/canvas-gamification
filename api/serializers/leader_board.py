from rest_framework import serializers

from course.models.models import LeaderBoardStudents, LeaderBoard

class LeaderBoardSerializer(serializers.ModelSerializer):
    
    def get_user(self):
        user = MyAnonymousUser()
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        return user
        
    def get_is_registered(self, course):
        user = self.get_user()
        # if user is not logged in or the request has no user attached
        if not user.is_authenticated:
            return False

        return course.is_registered(user)    
   
    class Meta:
        model = LeaderBoard
        fields = ['student', 'leader_board', 'token_value']

class LeaderBoardSerializerList(serializers.ModelSerializer):
    
    def get_user(self):
        user = MyAnonymousUser()
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        return user
            
    class Meta:
        model = LeaderBoard
        fields = ['student', 'leader_board', 'token_value']        
