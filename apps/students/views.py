from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, CreateView, UpdateView

from apps.classes.models import Classes
from apps.students.forms import StudentForm
from apps.students.models import Students


class AllStudentsListView(LoginRequiredMixin, ListView):
    model = Students
    template_name = "students/all_students.html"
    context_object_name = "students"
    ordering = ['-public_id']
    paginate_by = 20

@login_required
def add_student(request):
    form=StudentForm()
    classes = Classes.objects.all()
    context = {
        "form":form,
        "classes":classes,
    }
    return render(request,"students/student_add.html",context)

class StudentCreate(LoginRequiredMixin, CreateView):
    # specify the model for create view

    model = Students

    template_name = "students/students_form.html"
    # specify the fields to be displayed

    fields = ['name', 'father_name', 'gender', 'contact','fee', 'father_contact', 'address','classes', 'comments', 'admission_date','admission_end', "image", 'active']

    success_url ="/students/students/add/"

@login_required
def edit_student(request, student_id):
    form=StudentForm()
    student = Students.objects.get(id=student_id)
    classes = Classes.objects.all()
    context = {
        "form":form,
        "student":student,
        "classes":classes,
    }
    return render(request,"students/student_edit.html",context)

class StudentUpdate(LoginRequiredMixin, UpdateView):
    # specify the model for create view

    model = Students
    template_name = "students/students_form.html"
    # specify the fields to be displayed
    fields = ['name', 'father_name', 'gender', 'contact','fee', 'father_contact', 'address','classes', 'comments', 'admission_date','admission_end', "image", 'active']

    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Students, id=id_)
    success_url ="/students/"

@login_required
def view_student(request, student_id):
    student = Students.objects.get(id=student_id)
    classes = student.classes.all()
    context = {
        "student": student,
        "classes": classes,
    }
    return render(request, "students/view_student.html", context)

@login_required
def student_search(request):
    if request.method == "GET":
        search = request.GET.get("query")
        student_obj = Students.objects.filter(name=search)
        if student_obj:
            return render(request, "students/searched_student.html", {"student_name":student_obj})
        else:
            search = request.GET.get("query")
            try:
                student_obj_id = Students.objects.get(public_id=search)
                if student_obj_id:
                    return render(request, "students/searched_student.html", {"student_obj": student_obj_id})
            except:
                return HttpResponse("Incorrect Name or ID!")

@login_required
def active_inactive(request):
    students_active = Students.objects.filter(active=True)
    students_inactive = Students.objects.filter(active=False)

    context = {
        "students_active": students_active,
        "students_inactive": students_inactive,
    }
    return render(request, "students/active_inactive.html", context)

@login_required
def genders(request):
    male = Students.objects.filter(gender="Male")
    female = Students.objects.filter(gender="Female")

    context = {
        "male": male,
        "female": female,
    }
    return render(request, "students/genders.html", context)
