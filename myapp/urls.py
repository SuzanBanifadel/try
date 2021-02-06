# in myapp/urls.py
from django.urls import path
from .views import schools_list, students_list, classes_list, register_student

urlpatterns = [
    path("schools/", schools_list),
    path("schools/classes/", classes_list),
    path("schools/classes/students/", students_list),
    path("schools/<int:pk>/classes/<int:pk_class>/students/register/", register_student)
    #path("schools/{school_id}/classes/", school_classes),  
    #path("schools/{school_id}/classes/{class_id}", school_classes),      
    #path("schools/{school_id}/students/{student_id}/", student_detail)    
    #path("schools/{school_id}/", polls_list, name="polls_list"),
    #path("school/students/", polls_list, name="polls_list"),
    #path("schools/{school_id}/classes/{class_id}/students/{student_id}/", student_detail)    
]