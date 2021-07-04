from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apps.staff.models import Staff


@csrf_exempt
def api_delete_staff(request, staff_id):
    staff_obj = Staff.objects.get(pk=staff_id)
    staff_obj.delete()

    return JsonResponse({"success":True})