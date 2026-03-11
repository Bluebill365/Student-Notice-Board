from django.urls import path
from .views import (
    StudentCreateView,
    StudentListView,
    ImportStudentsView,
    ExportStudentsView,
)

urlpatterns = [
    path('add/', StudentCreateView.as_view(), name='student_add'),
    path('list/', StudentListView.as_view(), name='student_list'),
    path('import/', ImportStudentsView.as_view(), name='import_students'),
    path('export/', ExportStudentsView.as_view(), name='export_students'),
]