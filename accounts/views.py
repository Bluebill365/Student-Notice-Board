from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View
from .forms import SignupForm
from students.models import Student

class UserSignupView(View):
    template_name = 'accounts/signup.html'

    def get(self, request): # type: ignore
        form = SignupForm()
        return render(request, self.template_name, {'form': form}) # type: ignore

    def post(self, request): # type: ignore
        form = SignupForm(request.POST) # type: ignore
        if form.is_valid():
            try:
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                )

                Student.objects.create(
                    user=user,
                    full_name=form.cleaned_data['full_name'],
                    phone_number=form.cleaned_data['phone_number'],
                    index_number=form.cleaned_data['index_number'],
                    username=form.cleaned_data['username'],
                    gender=form.cleaned_data['gender'],
                    course=form.cleaned_data['course'],
                    level=form.cleaned_data['level'],
                    email=form.cleaned_data['email'],
                )

                login(request, user) # type: ignore
                messages.success(request, "Signup successful.") # type: ignore
                return redirect('dashboard')
            except Exception as e:
                messages.error(request, f"Signup failed: {e}") # type: ignore
        return render(request, self.template_name, {'form': form}) # type: ignore

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

class UserLogoutView(View):
    template_name = 'accounts/logout.html'

    def get(self, request): # type: ignore
        if not request.user.is_authenticated:
            messages.info(request, "You are already logged out.") # type: ignore
            return redirect('login')
        return render(request, self.template_name) # type: ignore

    def post(self, request): # type: ignore
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, "Logout successful.") # type: ignore
        else:
            messages.info(request, "You are already logged out.") # type: ignore
        return redirect('login')
