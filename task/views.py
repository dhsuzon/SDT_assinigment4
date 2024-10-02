from django.shortcuts import render,redirect
from .forms import TaskForm

def add_task(request):
    if request.method =='POST':
        Add_task = TaskForm(request.POST)
        if Add_task.is_valid():
            Add_task.save()
            return redirect('add_task')
    else:
        Add_task = TaskForm()
    return render(request,'add_task.html',{"form":Add_task})
