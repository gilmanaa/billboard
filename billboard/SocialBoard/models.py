from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=120)
    publish_date = models.DateField()
    content = models.CharField(max_length=500)
    author = models.CharField(max_length=24)
