from django.urls import path

from apps.staff.api import api_delete_staff
from apps.staff.views import AllStaffListView, add_staff, view_staff, edit_staff, StaffUpdate, StaffCreate, staff_search

urlpatterns = [
    path('', AllStaffListView.as_view(), name="all_staff"),
    path('add/', add_staff, name="add_staff"),
    #path('add/save/', add_staff_save, name="add_staff_save"),
    path('add/save/', StaffCreate.as_view(), name="add_staff_save"),
    path('view/<int:staff_id>/', view_staff, name="view_staff"),
    path('edit/<int:staff_id>/', edit_staff, name="edit_staff"),
    path('edit/save/<int:id>/', StaffUpdate.as_view(), name="edit_staff_save"),
    path('', view_staff, name="view_staff"),
    path('api/delete_staff/<int:staff_id>/', api_delete_staff, name="api_delete_staff"),
    path('staff-search/', staff_search, name="staff_search"),

]
