import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from apps.classes.models import Classes
from apps.income.models import Income
from apps.students.models import Students


@csrf_exempt
def api_delete_student(request, student_id):
    student_obj = Students.objects.get(pk=student_id)
    student_obj.delete()
    return JsonResponse({"success":True})

@csrf_exempt
def api_add_amount(request, student_id, class_id):
    student_obj = Students.objects.get(id=student_id)
    class_obj = Classes.objects.get(id=class_id)

    student_obj.admission_date = date.today()

    any_date = student_obj.admission_date
    next_month = any_date.replace(day=28) + datetime.timedelta(days=4)
    last_day_of_month = next_month - datetime.timedelta(days=next_month.day)

    student_obj.admission_end = last_day_of_month
    student_obj.save(update_fields=["admission_date", "admission_end"])
    fees = student_obj.fee

    income_obj = Income.objects.create(user=request.user, student=student_obj, amount=fees, date_added=date.today())
    income_obj.save()

    return render(request, "students/success.html")

