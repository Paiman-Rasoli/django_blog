from django.db import models

class Post(models.Model):
      id = models.AutoField(primary_key=True,)
      title = models.CharField(max_length=255)
      description = models.TextField(max_length=1000, null=True)