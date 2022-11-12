from django import forms
from secondapp.models import teacher

class teacherforms(forms.ModelForm):
    class Meta:
        model=teacher
        fields='__all__'