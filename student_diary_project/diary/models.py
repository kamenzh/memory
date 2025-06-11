from django.db import models
from django.contrib.auth.models import User

class Grade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    grade = models.FloatField()

    def __str__(self):
        return f"{self.subject}: {self.grade}"

class Absence(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.date} - {self.reason}"
