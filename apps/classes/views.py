from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from apps.classes.forms import ClassForm
from apps.classes.models import Classes
from apps.staff.models import Staff
from apps.students.models import Students


class AllClassesListView(LoginRequiredMixin,ListView):
    model = Classes
    template_name = "classes/all_classes.html"
    context_object_name = "classes"
    ordering = ['-end']
    paginate_by = 10

@login_required
def add_class(request):
    form=ClassForm()
    staffs = Staff.objects.all()
    context = {
        "form":form,
        "staffs":staffs,
    }
    return render(request,"classes/class_add.html",context)

@login_required
def add_class_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        form = ClassForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            room_no = form.cleaned_data["rom_no"]
            timing = form.cleaned_data["timing"]
            start = form.cleaned_data["start"]
            end = form.cleaned_data["end"]
            staff_id = form.cleaned_data["staff"]

            staff_ = Staff.objects.get(id=staff_id.id)

            class_object = Classes.objects.create(name=name, rom_no=room_no, timing=timing, start=start,
                                                  end=end, staff=staff_)
            class_object.save()
            context = {
                "form":form,
                'staffs':Staff.objects.all(),
             }
            return render(request, 'classes/class_add.html', context)
        else:
            form = ClassForm(request.POST)
            context = {
                "form":form
            }
            return render(request, 'classes/class_add.html', context)

@login_required
def view_class(request, class_id):
    class_obj = Classes.objects.get(id=class_id)
    students = Students.objects.filter(classes=class_obj)
    context = {
        "class_obj":class_obj,
        "students":students,
    }
    return render(request, "classes/view_class.html", context)

@login_required
def edit_class(request, class_id):
    class_obj = Classes.objects.get(id=class_id)
    staffs = Staff.objects.all()
    context = {
        "class_obj":class_obj,
        "staffs":staffs,
    }
    return render(request, "classes/class_edit.html", context)



@login_required
def edit_class_save(request, class_id):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        class_name = request.POST.get("name")
        class_room = request.POST.get("rom_no")
        class_timing = request.POST.get("timing")
        class_start = request.POST.get("start")
        class_end = request.POST.get("end")
        class_staff = request.POST.get("staff")
        staff=Staff.objects.get(id=class_staff)

        try:
            class_=Classes.objects.get(id=class_id)
            class_.name = class_name
            class_.rom_no = class_room
            class_.timing = class_timing
            class_.start = class_start
            class_.end = class_end
            class_.staff = staff
            class_.save()
            return HttpResponse('Class edited!')
        except:
            return HttpResponse('cant edit class!')


@login_required
def bill_list(request, student_id):
    student = Students.objects.get(pk=student_id)
    student_classes = student.classes.all()
    context = {
        "student":student,
        "student_classes":student_classes,
    }
    return render(request, "classes/student_bills.html", context)


@login_required
def bill_view(request, student_id, class_id):
    student = Students.objects.get(pk=student_id)
    class_obj = Classes.objects.get(pk=class_id)
    context = {
        "student":student,
        "class_obj":class_obj,
    }
    return render(request, "classes/bill_view.html", context)



@login_required
def class_search(request):
    if request.method == "GET":
        search = request.GET.get("query")
        class_obj = Classes.objects.filter(name=search)
        if class_obj:
            return render(request, "classes/searched_class.html", {"class_name":class_obj})
        else:
            search = request.GET.get("query")
            try:
                class_obj_id = Classes.objects.get(id=search)
                if class_obj_id:
                    return render(request, "classes/searched_class.html", {"class_obj":class_obj_id})
            except:
                return HttpResponse("Incorrect Name or ID!")


@login_required
def attendance_view(request, class_id):
    class_obj = Classes.objects.get(pk=class_id)
    students = Students.objects.filter(classes=class_obj.id)
    context = {
        "class_obj":class_obj,
        "students":students,
    }
    return render(request, "classes/attendance_view.html", context)



@login_required
def evaluation_view(request, class_id):
    class_obj = Classes.objects.get(pk=class_id)
    students = Students.objects.filter(classes=class_obj.id)
    context = {
        "class_obj":class_obj,
        "students":students,
    }
    return render(request, "classes/evaluation_view.html", context)



@login_required
def resultsheet_view(request, class_id):
    class_obj = Classes.objects.get(pk=class_id)
    students = Students.objects.filter(classes=class_obj.id)
    context = {
        "class_obj":class_obj,
        "students":students,
    }
    return render(request, "classes/resultsheet_view.html", context)



@login_required
def contactsheet_view(request, class_id):
    class_obj = Classes.objects.get(pk=class_id)
    students = Students.objects.filter(classes=class_obj.id)
    context = {
        "class_obj":class_obj,
        "students":students,
    }
    return render(request, "classes/contactsheet.html", context)

