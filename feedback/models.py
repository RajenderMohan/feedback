from django.db import models

class Feedback(models.Model):
    RATING_CHOICES = [(i, f'{i} Stars') for i in range(1, 6)]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.get_rating_display()}"