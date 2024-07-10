from django.contrib import admin
from django.urls import path, include
from . import views
from .views import profile, profile_edit
from .views import feedback
from .views import indexcourse


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),  # Include Django's authentication URLs
    path('signup/', views.signup, name='signup'),
    path('accounts/profile/', views.profile, name='profile'),  # Ensure the profile URL is defined like this
    path('assigned_courses/', views.assigned_courses, name='assigned_courses'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', profile_edit, name='profile_edit'),
    path('feedback/', feedback, name='feedback'),
    path('indexcourse',indexcourse, name="indexcourse")
]
