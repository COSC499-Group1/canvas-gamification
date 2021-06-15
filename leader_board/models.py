from django.db import models

# Create your models here.
import base64
import json
import random
from datetime import datetime

from django.db import models
from django.utils.crypto import get_random_string
from djrichtextfield.models import RichTextField
from polymorphic.models import PolymorphicModel

from accounts.models import MyUser
from canvas.models import Event, CanvasCourse
from course.fields import JSONField
from course.grader.grader import MultipleChoiceGrader, JunitGrader
from course.utils.junit_xml import parse_junit_xml
from course.utils.utils import get_token_value, ensure_uqj, calculate_average_success
from course.utils.variables import render_text, generate_variables
from general.models import Action



class Leader_Board(models.Model):
    name = models.TextField()
    is_visible = models.BooleanField(default = True)
    userId = models.ForeignKey(MyUser, on_delete = models.DO_NOTHING)
    courseId = models.ForeignKey(CanvasCourse,  related_name='%(class)s_requests_created' ,on_delete= models.DO_NOTHING)
    total_tokens_received = models.ForeignKey(CanvasCourse, on_delete = models.SET(0))
   
    def __str__(self):
      return self.name

    @property
    def is_leader_board(self):
        return self.is_leader_board       


class LeaderBoardAssignedStudents(models.Model):
    userId = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING)
    leader_board = models.ForeignKey(Leader_Board, on_delete=models.DO_NOTHING)