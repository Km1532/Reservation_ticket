from django.db import models

# Create your models here.
class Review(models.Model):
    user_name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_name} - {self.created_at}'