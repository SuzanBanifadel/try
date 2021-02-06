from django.db import models

# Create your models here.

class School(models.Model):
    school_id = models.AutoField(primary_key=True)
    school_name = models.CharField("School Name", max_length=255, blank=True, null=True)
    address = models.TextField("Address", blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    def __str__(self):
        return self.school_name

class Class(models.Model):
    class_id = models.AutoField(primary_key=True)
    school_id = models.ForeignKey(School,related_name="school_classes", on_delete=models.CASCADE)
    class_name = models.CharField(max_length=80)
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    def __str__(self):
        return self.class_name

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    school_id = models.ForeignKey(School, related_name="school_students", on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, related_name="class_students", on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    studentAge = models.IntegerField()
    def __str__(self):
        return self.student_name