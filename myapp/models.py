from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    students = models.ManyToManyField(User, related_name='courses', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Define the assigned_courses function outside the Course model class
def assigned_courses(request):
    # Get assigned courses for the current user
    assigned_courses = request.user.courses.all()
    
    return render(request, 'assigned_courses.html', {'assigned_courses': assigned_courses})

