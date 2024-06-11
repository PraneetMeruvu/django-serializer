from django.db import models

class Course(models.Model):
    course_program = models.CharField(max_length=50)
    course_code = models.CharField()
    course_name = models.CharField(max_length=255)
    elective = models.BooleanField()  

    def __str__(self):
        return f"{self.course_program}-{self.course_code}: {self.course_name}"
    