from django.db import models

# Create your models here.
class User(models.Model):
  student_name = models.CharField(max_length=50)
  teacher_name= models.CharField(max_length=60)
  email = models.EmailField(max_length=60)
  password = models.CharField(max_length=40)
  
