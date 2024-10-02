from django.db import models
from  category.models import CateoryModel

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    is_completed = models.BooleanField()
    Task_Assgin_Date = models.DateField(verbose_name="Task Assgin Date")
    category = models.ManyToManyField(CateoryModel)
    
    
    def __str__(self) :
        return  self.taskTitle
