from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Person(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?\d{10,15}$',
                message='Enter a valid phone number.'
            )
        ]
    )

    class Meta:
        abstract = True

class Student(Person):
    LEVEL_CHOICES = [
        ('100', 'Level 100'),
        ('200', 'Level 200'),
        ('300', 'Level 300'),
        ('400', 'Level 400'),
    ]

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    index_number = models.CharField(max_length=30, unique=True)
    username = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    course = models.CharField(max_length=100)
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.full_name} - {self.index_number}"