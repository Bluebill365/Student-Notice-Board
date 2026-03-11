from import_export import resources
from .models import Student

class StudentResource(resources.ModelResource): # type: ignore
    class Meta:
        model = Student
        fields = (
            'id',
            'full_name',
            'phone_number',
            'index_number',
            'username',
            'gender',
            'course',
            'level',
            'email',
        )
        export_order = fields