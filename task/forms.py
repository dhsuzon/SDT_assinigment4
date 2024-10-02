from django import forms
from .models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
     model = TaskModel
     fields = '__all__'
     
     widgets ={
         "Task_Assgin_Date": forms.DateInput(attrs={'type':'date'})
     }
     
     