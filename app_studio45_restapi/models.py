from django.db import models

class Student(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
    class Meta:
        db_table = 'students'

    def __str__(self):
        return self.title
# Create your models here.
