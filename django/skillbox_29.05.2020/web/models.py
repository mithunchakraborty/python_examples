from django.db import models


class Publication(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateTimeField(null=True)
    text = models.TextField()


class Comment(models.Model):
    publication = models.ForeignKey(
        Publication,
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(null=True)
    text = models.TextField()