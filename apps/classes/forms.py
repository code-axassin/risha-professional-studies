import datetime

from django import forms
from django.forms import ModelForm

from apps.classes.models import Classes
from apps.staff.models import Staff


"""class ClassForm(forms.Form):
    name=forms.CharField(label="Name",max_length=250)
    rom_no=forms.CharField(label="Room No.",max_length=250)
    timing=forms.TimeInput()
    start=forms.DateField(label="Start",widget=forms.DateInput(format='%d/%m/%Y'))
    end=forms.DateField(label="End",widget=forms.DateInput(format='%d/%m/%Y'))
    fees=forms.IntegerField(label="Fee")

    staff_list = []
    try:
        staffs = Staff.objects.all()
        for staff in staffs:
            staff_name = (staff.id, str(staff.name))
            staff_list.append(staff_name)
    except:
        cls_list = []
    staff = forms.ChoiceField(label="Staff", choices=staff_list, widget=forms.Select(attrs={"class": "form-control"}))
"""
class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%m-%d-%Y"
        super().__init__(**kwargs)


class TimeInput(forms.TimeInput):
    input_type = "time"
    def __init__(self, **kwargs):
        kwargs["format"] = "%H:%M"
        super().__init__(**kwargs)

class ClassForm(ModelForm):
    class Meta:
        model = Classes
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["start"].widget = DateInput()
        self.fields["end"].widget = DateInput()
        self.fields["timing"].widget = TimeInput()
    """
    def __init__(self, *args, **kwargs):
        super(ClassForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs['class'] = 'input'
        self.fields["rom_no"].widget.attrs['class'] = 'input'
        self.fields["timing"].widget.attrs['class'] = 'time'
        self.fields["start"].widget.attrs['DateField'] = 'DateInput'
        self.fields["fees"].widget.attrs['class'] = 'integer'
        self.fields["staff"].widget.attrs['class'] = 'select'

"""