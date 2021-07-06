  
from django.contrib.auth.models import AbstractUser
from django.db import models


class TwitterUser(AbstractUser):
    display_name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    following = models.ManyToManyField('self', symmetrical=False)

    def __str__(self):
        return self.display_name