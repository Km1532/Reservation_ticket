from django.db import models
from django.conf import settings
# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)  
    service = models.CharField(max_length=100, default='')  
    comment = models.TextField(default='')
    rating = models.IntegerField(default=0)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.created_at}'