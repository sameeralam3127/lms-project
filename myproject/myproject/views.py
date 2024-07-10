from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User


# View for the feedback page
def feedback(request):
    return render(request, 'feedback.html')

# View for the course page
def indexcourse(request):
    return render(request, 'course.html')

# View for the homepage
def index(request):
    return render(request, 'index.html')

# View for the user's profile page, requires login
@login_required
def profile(request):
    return render(request, 'profile.html')

# View for user signup
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data.get('email')  # Use get() to safely retrieve email
            
            # Check if username or email already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'A user with that username already exists.')
            elif email and User.objects.filter(email=email).exists():  # Check email only if provided
                messages.error(request, 'A user with that email already exists.')
            else:
                # Create the user if no existing user with the same username or email
                user = form.save()
                login(request, user)
                return redirect('login')  # Redirect to login page after successful signup
        else:
            # Handle form validation errors
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


# View for displaying assigned courses to the user
@login_required
def assigned_courses(request):
    assigned_courses = request.user.courses.all()
    return render(request, 'assigned_courses.html', {'assigned_courses': assigned_courses})

# View for editing user profile, requires login
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
