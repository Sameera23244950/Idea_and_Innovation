from django.db import models

class Idea(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
