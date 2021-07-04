from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from apps.classes.models import Classes
from apps.results.forms import ResultForm
from apps.results.models import Results
from apps.students.models import Students

class ResultClassList(LoginRequiredMixin, ListView):
    model = Classes
    context_object_name = "classes"
    template_name = "results/result_classes.html"
    paginate_by = 15

@login_required
def view_result_students(request, class_id):
    class_obj = Classes.objects.get(id=class_id)
    students = Students.objects.filter(classes=class_obj)
    context = {
        "class_obj" : class_obj,
        "students" : students,
    }
    return render(request, "results/view_result_students.html", context)

@login_required
def add_result(request, student_id, class_id):
    class_obj = Classes.objects.get(id=class_id)
    student = Students.objects.get(id=student_id)
    form = ResultForm()

    context = {
        "class_obj" : class_obj,
        "student" : student,
        "form" : form,
    }

    return render(request, "results/add_result.html", context)

class ResultCreate(LoginRequiredMixin, CreateView):
    model = Results
    fields = ['student', 'class_name', 'date', 'marks', 'position']

    def get_success_url(self):
        return reverse('view_result_students', kwargs={'class_id': self.object.class_name.id})


@login_required
def result_list(request, class_id):
    class_obj = Classes.objects.get(id=class_id)
    results = Results.objects.filter(class_name=class_obj.id)
    context = {
        "class_obj" : class_obj,
        "results" : results,
    }
    return render(request, "results/all_results.html", context)


@login_required
def update_result(request, result_id):
    result = Results.objects.get(id=result_id)
    context = {
        "result" : result,
    }
    return render(request, "results/update_result.html", context)

class ResultUpdate(LoginRequiredMixin, UpdateView):
    model = Results
    fields = ['date', 'marks', 'position']
    template_name = 'students/students_form.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Results, id=id_)

    def get_success_url(self):
        return reverse('view_results', kwargs={'class_id': self.object.class_name.id})

@login_required
def print_view(request, class_id):
    class_obj = Classes.objects.get(id=class_id)
    results = Results.objects.filter(class_name=class_obj.id)
    p = Paginator(results, 6)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    # sending the page object to index.html
    context = {
        "class_obj": class_obj,
        'page_obj': page_obj
    }
    return render(request, "results/specific_result.html", context)

@login_required
def result_search_classes(request):
    if request.method == "GET":
        search = request.GET.get("query")
        class_obj = Classes.objects.filter(name=search)
        if class_obj:
            return render(request, "results/searched_result_class.html", {"class_name":class_obj})
        else:
            search = request.GET.get("query")
            try:
                class_obj_id = Classes.objects.get(id=search)
                if class_obj_id:
                    return render(request, "results/searched_result_class.html", {"class_obj":class_obj_id})
            except:
                return HttpResponse("Incorrect Name or ID!")

@login_required
def result_search(request):
    if request.method == "GET":
        search = request.GET.get("query")
        try:
            student = Students.objects.get(public_id=search)
            if student:
                results = Results.objects.filter(student=student)
                context = {
                    "student" : student,
                    "results" : results,
                }
                return render(request, "results/searched_result.html", context)
            else:
                return HttpResponse("Incorrect Name or ID!")

        except:
            return HttpResponse("Incorrect Name or ID!")
