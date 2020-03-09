import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question


class QuestionModelTests(TestCase):

    def test_published_recently_with_recent_question(self):
        pub_date = timezone.now() - datetime.timedelta(seconds=30)
        recent_question = Question(pub_date=pub_date)
        self.assertIs(expr1=True, expr2=recent_question.was_published_recently())

    def test_published_recently_with_old_question(self):
        pub_date = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=pub_date)
        self.assertIs(expr1=False, expr2=old_question.was_published_recently())

    def test_published_recently_with_future_question(self):
        pub_date = timezone.now() + datetime.timedelta(days=1)
        future_question = Question(pub_date=pub_date)
        self.assertIs(expr1=False, expr2=future_question.was_published_recently())
