from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView

from apps.staff.forms import AddStaffForm
from apps.staff.models import Staff


class AllStaffListView(LoginRequiredMixin, ListView):
    model = Staff
    template_name = "staff/all_staff.html"
    context_object_name = "staff"
    ordering = ['-id']
    paginate_by = 20

@login_required
def add_staff(request):
    form = AddStaffForm()
    context = {
        "form":form,
    }
    return render(request,"staff/add_staff.html", context)

class StaffCreate(LoginRequiredMixin, CreateView):
    model = Staff
    fields = ['name', 'contact', 'cv', 'comments', "image"]
    template_name = 'students/students_form.html'
    success_url = "/staff/"

@login_required
def view_staff(request, staff_id):
    staff = Staff.objects.get(id=staff_id)
    context = {
        "staff" : staff,
    }
    return render(request, "staff/view_staff.html", context)


@login_required
def edit_staff(request, staff_id):
    staff = Staff.objects.get(id=staff_id)
    context = {
        'staff':staff,
    }
    return render(request, 'staff/edit_staff.html', context)

class StaffUpdate(LoginRequiredMixin, UpdateView):
    # specify the model for create view

    model = Staff
    template_name = 'students/students_form.html'
    #template_name = "staff/edit_staff.html"
    # specify the fields to be displayed
    fields = ['name', 'contact', 'comments', "image"]
    success_url = "/staff/"


    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Staff, id=id_)

@login_required
def staff_search(request):
    if request.method == "GET":
        search = request.GET.get("query")
        staff_obj = Staff.objects.filter(name=search)
        if staff_obj:
            return render(request, "staff/searched_staff.html", {"staff_name": staff_obj})
        else:
            search = request.GET.get("query")
            try:
                staff_obj_id = Staff.objects.get(id=search)
                if staff_obj_id:
                    return render(request, "staff/searched_staff.html", {"staff_obj": staff_obj_id})
            except:
                return HttpResponse("Incorrect Name or ID!")

