from django.db import models
from students.models import Student

class Notice(models.Model):
    NOTICE_TYPE_CHOICES = [
        ('all', 'All Students'),
        ('level', 'Specific Level'),
        ('selected', 'Selected Students'),
        ('single', 'One Student'),
    ]

    title = models.CharField(max_length=200)
    message = models.TextField()
    notice_type = models.CharField(max_length=20, choices=NOTICE_TYPE_CHOICES)
    target_level = models.CharField(max_length=10, blank=True, null=True)
    target_students = models.ManyToManyField(Student, blank=True) # type: ignore
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title