from django.db import models

class BoardModel(models.Model):
  title = models.CharField(max_length = 100)
  content = models.TextField()
  author = models.CharField(max_length = 100)
  images = models.ImageField(upload_to='')
  good = models.IntegerField(null=True, blank=True, default=0)
  read = models.IntegerField(null=True, blank=True, default=0)
  goodtext = models.CharField(max_length = 200, null=True, blank=True, default='a')
  readtext = models.CharField(max_length = 200, null=True, blank=True, default='a')