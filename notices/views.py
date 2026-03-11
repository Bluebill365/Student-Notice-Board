from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render # type: ignore
from django.views.generic import CreateView, ListView
from .forms import NoticeForm
from .models import Notice
from students.models import Student

class NoticeCreateView(LoginRequiredMixin, CreateView):
    model = Notice
    form_class = NoticeForm
    template_name = 'notices/notice_forms.html'
    success_url = '/notices/list/'

    def form_valid(self, form): # type: ignore
        try:
            messages.success(self.request, "Notice created successfully.")
            return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, f"Error creating notice: {e}")
            return self.form_invalid(form)

class NoticeListView(LoginRequiredMixin, ListView):
    model = Notice
    template_name = 'notices/notice_list.html'
    context_object_name = 'notices'
    ordering = ['-created_at']

class DashboardView(LoginRequiredMixin, ListView):
    model = Notice
    template_name = 'notices/dashboard.html'
    context_object_name = 'notices'

    def get_queryset(self):
        try:
            student = Student.objects.get(user=self.request.user)
            return Notice.objects.filter(
                Q(notice_type='all') |
                Q(notice_type='level', target_level=student.level) |
                Q(target_students=student)
            ).distinct().order_by('-created_at')
        except Student.DoesNotExist:
            return Notice.objects.none()
        except Exception:
            return Notice.objects.none()
