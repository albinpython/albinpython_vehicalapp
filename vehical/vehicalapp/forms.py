from . models import CRUD
from django import forms

class Todoforms(forms.ModelForm):
    class Meta:
        model=CRUD
        fields=['Vehicle_Number','Vehicle_type','Vehicle_model','Vehicle_description']