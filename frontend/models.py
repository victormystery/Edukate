from django.db import models

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField()
   
    def __str__(self):
       return self.title
class Instructor(models.Model):
    name = models.CharField(max_length=250)
    subject_taken = models.ForeignKey('Subject', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Grade(models.Model):
    grade = models.CharField(max_length=50)
    
    def __str__(self):
        return self.grade
class Student(models.Model):
    name = models.CharField(max_length=250)
    grade_class = models.ForeignKey('Grade', on_delete=models.CASCADE)
    D_o_B = models.DateField()
    address = models.TextField()
    def __str__(self):
        return self.name
    

   
