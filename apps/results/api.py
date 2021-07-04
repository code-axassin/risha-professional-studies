from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apps.results.models import Results


@csrf_exempt
def api_delete_result(request, result_id):
    result_obj = Results.objects.get(pk=result_id)
    result_obj.delete()

    return JsonResponse({"success":True})