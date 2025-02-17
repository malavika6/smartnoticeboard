from django.db import models

# Models


class Notice(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class AdminUser(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
