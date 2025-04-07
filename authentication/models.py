from django.contrib.auth.models import AbstractUser
from django.db import models
from utils.choices import Gender, Role


class CustomUser(AbstractUser):
    dob = models.DateField(null=True, blank=True)
    contact_no = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=Gender.choices)
    profile_photo = models.ImageField(upload_to='profiles/', null=True, blank=True)
    role = models.CharField(max_length=20, choices=Role.choices)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'dob', 'contact_no', 'role']

    def __str__(self):
        return f"{self.username} ({self.role})"
