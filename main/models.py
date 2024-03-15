from django.db import models

# Create your models here.
class Review(models.Model):
    nickname = models.CharField(max_length=100, default='')  
    service = models.CharField(max_length=100, default='')  
    comment = models.TextField(default='')
    rating = models.IntegerField(default=0)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nickname} - {self.created_at}'