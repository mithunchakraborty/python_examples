from django.db import models


class Articles(models.Model):
    pub_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    text = models.TextField()