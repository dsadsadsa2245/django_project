from django.db import models
class Student(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    age=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name='student'
        verbose_name_plural='students'

    def __str__(self):
        return self.first_name
class Course(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    students=models.ManyToManyField(Student,related_name='students')
    class Meta:
        verbose_name='Course'
        verbose_name_plural='courses'

    def __str__(self):
        return self.name

