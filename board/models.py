from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    author = models.CharField(max_length=30)
    image = models.ImageField(blank=True, null=True, upload_to='')
    read = models.IntegerField(default=0)
    readtext = models.CharField(max_length=200)

    def __str__(self):
        return self.title
