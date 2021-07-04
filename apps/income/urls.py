from django.urls import path

from apps.income.views import AllIncomeListView

urlpatterns = [
    path('', AllIncomeListView.as_view(), name="all_income"),
]