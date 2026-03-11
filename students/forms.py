from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'full_name',
            'phone_number',
            'index_number',
            'username',
            'gender',
            'course',
            'level',
            'email',
        ]

    def clean_index_number(self):
        index_number = self.cleaned_data['index_number']
        qs = Student.objects.filter(index_number=index_number)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Index number already exists.")
        return index_number

    def clean_email(self):
        email = self.cleaned_data['email']
        qs = Student.objects.filter(email=email)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Email already exists.")
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        qs = Student.objects.filter(username=username)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("Username already exists.")
        return username