from django import forms
from django.forms import ModelForm, Textarea

from apps.students.models import Students

class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%m-%d-%Y"
        super().__init__(**kwargs)



class StudentForm(ModelForm):
    class Meta:
        model = Students
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["admission_date"].widget = DateInput()
        self.fields["admission_end"].widget = DateInput()
        self.fields["image"].widget = forms.ImageField()
        self.fields["active"].widget = forms.BooleanField()
