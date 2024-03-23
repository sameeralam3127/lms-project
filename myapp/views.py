from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
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
            return redirect('index')  # Redirect to index page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
