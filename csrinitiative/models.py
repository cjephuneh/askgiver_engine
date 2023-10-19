from django.db import models

# Create your models here.

class CsrInitiative(models.Model):
    Orgname = models.CharField(max_length=100)
    Orgtype = models.EmailField()
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    initiative = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    # is_active = models.BooleanField(default=True)
    # is_admin = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)
    # is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name