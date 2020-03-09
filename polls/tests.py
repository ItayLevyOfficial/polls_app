import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question


class QuestionModelTests(TestCase):

    def test_published_recently_with_future_question(self):
        publish_time = timezone.now() + datetime.timedelta(days=1)
        future_question = Question(pub_date=publish_time)
        self.assertIs(expr1=False, expr2=future_question.was_published_recently())
