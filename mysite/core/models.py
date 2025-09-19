from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']

class Student(models.Model):
    COURSE_CHOICES = [
        ('CS', 'Computer Science'),
        ('EE', 'Electrical Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('CE', 'Civil Engineering'),
        ('BIO', 'Biology'),
        ('CHEM', 'Chemistry'),
        ('PHYS', 'Physics'),
        ('MATH', 'Mathematics'),
        ('ENG', 'English'),
        ('HIST', 'History'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=10, choices=COURSE_CHOICES)
    grades = models.DecimalField(max_digits=5, decimal_places=2, help_text="GPA out of 4.00")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} - {self.course}"
    
    class Meta:
        ordering = ['name']
