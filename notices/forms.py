from django import forms
from .models import Notice

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'message', 'notice_type', 'target_level', 'target_students']
        widgets = {
            'target_students': forms.CheckboxSelectMultiple(),
        }

    def clean(self):
        cleaned_data = super().clean()
        notice_type = cleaned_data.get('notice_type')
        target_level = cleaned_data.get('target_level')
        target_students = cleaned_data.get('target_students')

        if notice_type == 'level' and not target_level:
            raise forms.ValidationError("Target level is required for level notices.")

        if notice_type == 'selected' and not target_students:
            raise forms.ValidationError("Select at least one student.")

        if notice_type == 'single':
            if not target_students or len(target_students) != 1:
                raise forms.ValidationError("Select exactly one student for single notice.")

        return cleaned_data