from django.contrib.auth.decorators import login_required  # Import login_required decorator
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import login


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
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def assigned_courses(request):
    # Get assigned courses for the current user
    assigned_courses = request.user.courses.all()
    
    return render(request, 'assigned_courses.html', {'assigned_courses': assigned_courses})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after saving changes
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'profile_edit.html', {'form': form})
   

   