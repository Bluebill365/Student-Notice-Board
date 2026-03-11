from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home_redirect(request): # type: ignore
    return redirect('dashboard')

urlpatterns = [ # type: ignore
    path('admin/', admin.site.urls),
    path('', home_redirect, name='home'), # type: ignore
    path('accounts/', include('accounts.urls')),
    path('students/', include('students.urls')),
    path('notices/', include('notices.urls')),
]