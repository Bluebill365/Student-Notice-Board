from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Student

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin): # type: ignore
    list_display = ('full_name', 'index_number', 'level', 'course', 'email')
    search_fields = ('full_name', 'index_number', 'email', 'level')