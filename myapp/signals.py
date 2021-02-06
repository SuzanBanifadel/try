''' just a trial :(
from .models import Student
from django.http import JsonResponse,HttpResponse

def create_student(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)
        return JsonResponse("Created")

def save_student(sender, instance, **kwargs):
    instance.myapp.save()
    return JsonResponse("Saved")


return JsonResponse({'student_id':new_student.student_id,
                            'student_name':studentName,
                             'studentAge':studentAge,
                             'school_id':school.school_id,
                             'class_id':sclass.class_id,
        })    '''

