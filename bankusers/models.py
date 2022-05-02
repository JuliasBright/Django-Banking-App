from django.db import models

# Create your models here.

class Bankuser(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    user_name = models.CharField(max_length=100)
    user_surname = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.user_name
