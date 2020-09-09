from django.db import models
from web_app.models import Job_postings


class Question(models.Model):
    """Question model."""

    job = models.ForeignKey(
        Job_postings,
        on_delete=models.CASCADE,
        related_name='questions')
    question = models.CharField(max_length=10000)

    def __str__(self):
        return self.question


class Option(models.Model):
    """Option model."""

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='options')
    option = models.CharField(max_length=1000)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.question.question} - {self.option}'
