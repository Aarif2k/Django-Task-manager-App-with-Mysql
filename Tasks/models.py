from django.db import models

# Create your models here.

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.title} ({self.status})"


