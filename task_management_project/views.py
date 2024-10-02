from django.shortcuts import render,redirect
from task.models import TaskModel
from task.forms import TaskForm


def  Taskview(request):
    task_show = TaskModel.objects.all()
    return render(request, 'task_show.html',{"data":task_show})



def Task_edit(request, id):
     edit = TaskModel.objects.get(pk=id)
    
     if request.method =='POST':
        edit_task = TaskForm(request.POST, instance=edit)
        if edit_task.is_valid():
            edit_task.save()  
            return redirect('task_show') 
     else:
        edit_task = TaskForm(instance=edit)
     return render(request, 'add_task.html', {"form": edit_task})



    
def Task_delete(request, id):
     delete_task = TaskModel.objects.get(pk=id)
     delete_task.delete()
     return redirect("task_show")
    
    