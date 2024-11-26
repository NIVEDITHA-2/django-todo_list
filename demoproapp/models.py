from django.db import models

# Create your models here.
class Task(models.Model):
    task_title=models.CharField(max_length=250)
    task_description=models.TextField(max_length=300)
    time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.task_title