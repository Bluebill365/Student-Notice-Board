import tablib
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView, ListView
from .forms import StudentForm
from .models import Student
from .resources import StudentResource

class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = '/students/list/'

    def form_valid(self, form): # type: ignore
        try:
            messages.success(self.request, "Student added successfully.")
            return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, f"Error saving student: {e}")
            return self.form_invalid(form)

class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'

class ImportStudentsView(LoginRequiredMixin, View):
    template_name = 'students/import_students.html'

    def get(self, request): # type: ignore
        return render(request, self.template_name) # type: ignore

    def post(self, request): # type: ignore
        if 'student_file' not in request.FILES: # type: ignore
            messages.error(request, "No file uploaded.") # type: ignore
            return redirect('import_students')

        student_file = request.FILES['student_file'] # type: ignore

        if not student_file.name.endswith('.csv'): # type: ignore
            messages.error(request, "Only CSV files are supported.") # type: ignore
            return redirect('import_students')

        try:
            dataset = tablib.Dataset().load(student_file.read().decode('utf-8'), format='csv') # type: ignore
            resource = StudentResource()
            result = resource.import_data(dataset, dry_run=True)

            if result.has_errors():
                messages.error(request, "Import contains errors. Fix the CSV and try again.") # type: ignore
                return redirect('import_students')

            resource.import_data(dataset, dry_run=False)
            messages.success(request, "Students imported successfully.") # type: ignore
        except Exception as e:
            messages.error(request, f"Import failed: {e}") # type: ignore

        return redirect('student_list')

class ExportStudentsView(LoginRequiredMixin, View):
    def get(self, request): # type: ignore
        try:
            resource = StudentResource()
            dataset = resource.export() # type: ignore
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="students.csv"'
            return response
        except Exception as e:
            messages.error(request, f"Export failed: {e}") # type: ignore
            return redirect('student_list')