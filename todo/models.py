from django.db import models

# Create your models here.

class TodoModel(models.Model):
    task = models.CharField(max_length=500 ,default='')
    status=models.CharField(max_length=500,default='')
    PRIORITY_CHOICES = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Less', 'Less'),
    )
    Priority =models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='')
    Date=models.DateField(auto_now_add=True)


