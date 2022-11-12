from django import forms
from firstapp.models import students

class studentforms(forms.ModelForm):
    class Meta:
        model=students
        fields='__all__'