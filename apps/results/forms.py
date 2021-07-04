from django import forms
from django.forms import ModelForm

from apps.results.models import Results


class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%m-%d-%Y"
        super().__init__(**kwargs)

class ResultForm(ModelForm):
    class Meta:
        model = Results
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["date"].widget = DateInput()