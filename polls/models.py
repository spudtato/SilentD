import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class Questions(models.Model):
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.publish_date >= timezone.now() - datetime.timedelta(days=1)

    question_text = models.CharField(max_length=250)
    publish_date = models.DateTimeField('date published')

class Answers(models.Model):
    def __str__(self):
        return self.choice_test
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    choice_test = models.CharField(max_length=250)
    votes = models.IntegerField(default=0)

