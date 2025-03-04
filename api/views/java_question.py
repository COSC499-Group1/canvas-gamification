from rest_framework import viewsets

from api.pagination import BasePagination
from api.permissions import TeacherAccessPermission
from api.serializers import JavaQuestionSerializer
from course.models.java import JavaQuestion


class JavaQuestionViewSet(viewsets.ModelViewSet):
    queryset = JavaQuestion.objects.all()
    permission_classes = [TeacherAccessPermission]
    serializer_class = JavaQuestionSerializer
    pagination_class = BasePagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
