from django.db import models

class Article(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

