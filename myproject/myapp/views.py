<<<<<<< HEAD
from django.contrib.auth.decorators import login_required  # Import login_required decorator
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Course

def index(request):
    return render(request, 'index.html')

@login_required
def profile(request):
    return render(request, 'profile.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect to index page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def assigned_courses(request):
    # Get assigned courses for the current user
    assigned_courses = request.user.courses.all()
    
=======
from django.contrib.auth.decorators import login_required  # Import login_required decorator
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Course

def index(request):
    return render(request, 'index.html')

@login_required
def profile(request):
    return render(request, 'profile.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirect to index page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def assigned_courses(request):
    # Get assigned courses for the current user
    assigned_courses = request.user.courses.all()
    
>>>>>>> edb0d550bb3b14100fe77431cd9e7433f0c5f397
    return render(request, 'assigned_courses.html', {'assigned_courses': assigned_courses})