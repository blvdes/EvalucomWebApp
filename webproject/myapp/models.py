from django.db import models

class Review(models.Model):
    movieID = models.CharField(max_length=15)
    score = models.IntegerField()
    text = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']
    