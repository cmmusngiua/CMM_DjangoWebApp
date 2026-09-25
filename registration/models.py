from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    year_level = models.IntegerField(default=1)
    email = models.EmailField()

    def __str__(self):
        return self.student_name