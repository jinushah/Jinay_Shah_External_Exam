from django.db import models

# Create your models here.
class TodoTask(models.Model):
    task = models.TextField(max_length=1500,default="")

    def __str__(self):
        return self.task