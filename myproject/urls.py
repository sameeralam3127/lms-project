from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),  # Include Django's authentication URLs
    path('signup/', views.signup, name='signup'),
    path('accounts/profile/', views.profile, name='profile'),  # Ensure the profile URL is defined like this
    path('assigned_courses/', views.assigned_courses, name='assigned_courses'),
]
