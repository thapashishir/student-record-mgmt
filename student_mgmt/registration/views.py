import re
from django.shortcuts import render, redirect
from django.views.generic import View
from . models import Student

# Create your views here.
class StudentListView(View):
    def get(self, request, *args, **kwargs):
        students=Student.objects.all()
        context = {
            "students" : students
        }
        return render(request, "registration/student_list.html", context)


class StudentAddView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "registration/student_add.html")
    
    def post(self, request, *args, **kwargs):
        data = {
            "student_name": request.POST.get("student_name"),
            "roll_no": request.POST.get("roll_no"),
            "gender": request.POST.get("gender"),
            "faculty": request.POST.get("faculty"),
        } 
        student=Student.objects.create(**data)
        student.save()
        return redirect('/student/list')


class StudentEditView(View):
    def get(self, request, *args, **kwargs):
        url_parmeter = self.kwargs
        student_id = url_parmeter["student_id"]
        student=Student.objects.get(student_id=student_id)
        context = {
            "student" : student
        }
        return render(request, "registration/student_edit.html", context)
    
    def post(self, request, *args, **kwargs):
        data = {
            "student_name": request.POST.get("student_name"),
            "roll_no": request.POST.get("roll_no"),
            "gender": request.POST.get("gender"),
            "faculty": request.POST.get("faculty"),
        } 
        Student.objects.filter(student_id = request.POST.get("student_id")).update(**data)
        return redirect('/student/list')


class StudentDeleteView(View):
    def get(self, request, *args, **kwargs):
        url_parmeter = self.kwargs
        student_id = url_parmeter["student_id"]
        Student.objects.filter(student_id = student_id).delete()
        return redirect("/student/list")
    

