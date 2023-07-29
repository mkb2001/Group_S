from django.db import models


# Create your models here.
class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    instructor_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    course_unit = models.CharField(max_length=100)
    knowledge = models.CharField(max_length=100)
    communication = models.CharField(max_length=100)
    teaching_style = models.CharField(max_length=100)
    responsiveness = models.CharField(max_length=100)
    additional_comments = models.CharField(max_length=100)
