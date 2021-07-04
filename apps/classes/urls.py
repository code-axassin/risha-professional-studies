from django.urls import path

from apps.classes.api import api_delete_class
from apps.classes.views import AllClassesListView, add_class, add_class_save, view_class, edit_class, edit_class_save, \
    bill_list, bill_view, class_search, attendance_view, evaluation_view, resultsheet_view, contactsheet_view
from apps.students.api import api_add_amount

urlpatterns = [
    path('', AllClassesListView.as_view(), name="all_classes"),
    path('classes/add', add_class, name="add_class"),
    path('classes/save', add_class_save, name="add_class_save"),
    path('<int:class_id>/', view_class, name="view_class"),
    path('edit/<int:class_id>/', edit_class, name="edit_class"),
    path('edit/<int:class_id>/save', edit_class_save, name="edit_class_save"),
    path('api/delete_class/<int:class_id>/', api_delete_class, name="api_delete_class"),
    path('bill-list/<int:student_id>/', bill_list, name= "bill_list"),
    path('bill-view/<int:student_id>/<int:class_id>/', bill_view, name= "bill_view"),
    path('api/add_amount/<int:student_id>/<int:class_id>/', api_add_amount, name="api_add_amount"),
    path('search-class/', class_search, name="class_search"),
    path('attendance/<int:class_id>/', attendance_view, name="attendance_view"),
    path('evaluation/<int:class_id>/', evaluation_view, name="evaluation_view"),
    path('resultsheet/<int:class_id>/', resultsheet_view, name="resultsheet_view"),
    path('contactsheet/<int:class_id>/', contactsheet_view, name="contactsheet_view"),

]