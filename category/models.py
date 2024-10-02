from django.db import models

class CateoryModel(models.Model):
    category_name= models.CharField(max_length=1000,verbose_name="Category Name")
    
    def __str__(self):
       return self.category_name
   