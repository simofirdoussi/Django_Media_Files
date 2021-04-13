from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 100, null=True)
    headline = models.TextField(null=True)
    image = models.ImageField(upload_to='images/', null=True)
    content = models.TextField()
