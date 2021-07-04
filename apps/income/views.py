from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from apps.income.models import Income



class AllIncomeListView(LoginRequiredMixin, ListView):
    model = Income
    template_name = "income/all_income.html"
    context_object_name = "incomes"
    ordering = ['-date_added']
    paginate_by = 30

"""
def view_income(request):
    incomes = Income.objects.all()
    context = {
        "incomes":incomes,
    }
    return render(request, "income/all_income.html", context)"""