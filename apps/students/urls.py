from django.urls import path

from apps.students.api import api_delete_student
from apps.students.views import AllStudentsListView, add_student, StudentCreate, view_student, StudentUpdate, \
    edit_student, student_search, active_inactive, genders

urlpatterns = [
    path('', AllStudentsListView.as_view(), name="all_students"),
    path('students/add/', add_student, name="add_student"),
    path('students/add/save', StudentCreate.as_view(), name="add_student_save"),
    path('students/<int:student_id>', view_student, name="view_student"),
    path('api/delete_student/<int:student_id>/', api_delete_student, name="api_delete_student"),
    path('students/edit/<int:student_id>', edit_student, name="edit_student"),
    path('students/edit/save/<int:id>/', StudentUpdate.as_view(), name="edit_student_save"),
    path('student-search/', student_search, name="student_search"),
    path('active-inactive/', active_inactive, name="active_inactive"),
    path('genders/', genders, name="genders"),

]