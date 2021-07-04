from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from apps.classes.models import Classes

@csrf_exempt
def api_delete_class(request, class_id):
    class_obj = Classes.objects.get(pk=class_id)
    class_obj.delete()

    return JsonResponse({"success":True})