from django.urls import path

from apps.results.api import api_delete_result
from apps.results.views import add_result, view_result_students, ResultCreate, update_result, \
    result_list, ResultUpdate, ResultClassList, print_view, result_search_classes, result_search

urlpatterns = [
    path('', ResultClassList.as_view(), name="show_classes"),
    path('view-students/<int:class_id>/', view_result_students, name="view_result_students"),
    path('add/<int:student_id>//<int:class_id>/', add_result, name="add_result"),
    path('add/save/', ResultCreate.as_view(), name="add_result_save"),
    path('results/<int:class_id>/', result_list, name="view_results"),
    path('update/<int:result_id>/', update_result, name="update_result"),
    path('update/save/<int:id>/', ResultUpdate.as_view(), name="update_result_save"),
    path('api/delete_result/<int:result_id>/', api_delete_result, name="delete_result"),
    path('print-results/<int:class_id>/', print_view, name="print_view"),
    path('search-result-classes/', result_search_classes, name="result_search_classes"),
    path('search-result/', result_search, name="result_search"),
    path('search-result/', result_search, name="result_search"),
]