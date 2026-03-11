from django import forms
from django.contrib.auth.models import User
from students.models import Student

class SignupForm(forms.ModelForm):
    full_name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=15)
    index_number = forms.CharField(max_length=30)
    gender = forms.ChoiceField(choices=Student.GENDER_CHOICES)
    course = forms.CharField(max_length=100)
    level = forms.ChoiceField(choices=Student.LEVEL_CHOICES)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists.")
        if Student.objects.filter(username=username).exists():
            raise forms.ValidationError("Student username already exists.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        if Student.objects.filter(email=email).exists():
            raise forms.ValidationError("Student email already exists.")
        return email

    def clean_index_number(self):
        index_number = self.cleaned_data['index_number']
        if Student.objects.filter(index_number=index_number).exists():
            raise forms.ValidationError("Index number already exists.")
        return index_number

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data