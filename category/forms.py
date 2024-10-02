from django import forms
from .models import CateoryModel

class CategoryForm(forms.ModelForm):
    class Meta:
        model = CateoryModel
        fields ='__all__'