from django.http import JsonResponse,HttpResponse
import json
from .models import School, Class, Student
from django.db.models.signals import post_save
from django.core.signals import request_finished
from django.dispatch import receiver
from django.contrib.auth.models import User


#List All Schools
def schools_list(request):
    schools = School.objects.all()
    data = {"All Schools": list(schools.values("school_id","school_name", "address", "created_at"))}
    return JsonResponse(data)
#List All Classes
def classes_list(request):
    classes = Class.objects.all()
    data = {"All Classes": list(classes.values("school_id","class_id","class_name", "created_at"))}
    return JsonResponse(data)
#List All Students
def students_list(request):
    students = Student.objects.all()
    data = {"All Students": list(students.values( "school_id","class_id","student_id","student_name","studentAge", "created_at"))}
    return JsonResponse(data)

#All Classes Of a Specific School        
def school_classes(request, pk):
    if request.method == 'GET':
        school = School.objects.get(pk =pk)
        schoolClasses =  school.school_classes.all()
        data = {school.school_name: list(schoolClasses.values("school_id","class_id","class_name", "created_at"))}       
        return JsonResponse(data)
#All Students Of a Specific School        
def school_students(request, pk):
    if request.method == 'GET':
        school = School.objects.get(pk =pk)
        schoolStudents =  school.school_students.all()
        data = {school.school_name: list(schoolStudents.values("school_id", "class_id", "student_id", "student_name", "studentAge", "created_at"))}       
        return JsonResponse(data)        
#Register New Student at a Specific School and a Specific Class
def register_student(request, pk, pk_class):
    if request.method == 'POST':
        school = School.objects.get(pk = pk)
        sclass = Class.objects.get(pk = pk_class)
        studentName = request.POST.get('student_name')
        studentAge = request.POST.get('studentAge')
        new_student = Student(school_id_id = school.school_id,class_id_id = sclass.class_id,student_name = studentName ,studentAge = studentAge)
        new_student.save()
        return JsonResponse({'student_id':new_student.student_id,
                            'student_name':studentName,
                             'studentAge':studentAge,
                             'school_id':school.school_id,
                             'class_id':sclass.class_id,
        })

#Signal Fires Every request
@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")

#signal Fires Every New Student Regestration
@receiver(post_save, sender=Student)
def show_student_data(sender, **kwargs):
    if kwargs.get('created', False):
        new_student = Student.objects.last()
        print("Model Student Affected!")
        print("student_id: {} ,student_name: {} , studentAge: {},school_id: {} ,class_id: {} ".format(new_student.student_id, new_student.student_name,new_student.studentAge,new_student.school_id,new_student.class_id_id) )
