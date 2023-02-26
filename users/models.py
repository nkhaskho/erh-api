from django.db import models


USER_ROLES = [
    ('superuser', 'Super admin'),
    ('admin', 'Enterprise admin'),
    ('employee', 'Enterprise employee')
]

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    fullname = models.CharField(max_length=20, default="")
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=USER_ROLES)

    def __str__(self) -> str:
        return self.fullname.capitalize()
    

