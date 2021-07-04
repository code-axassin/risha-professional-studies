from django import forms
from django.forms import ModelForm
from apps.staff.models import Staff

"""
class AddStaffForm(forms.Form):
    name = forms.CharField(label="NameD", max_length=250,widget=forms.TextInput())
    contact = forms.IntegerField(label="Contact",widget=forms.NumberInput())
    cv = forms.FileField(label="C.V", max_length=250,widget=forms.FileInput())
    comments = forms.CharField(label="Comments", max_length=250,widget=forms.TextInput())
    image = forms.FileField(label="Image", max_length=250,widget=forms.FileInput())
"""
class AddStaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["cv"].widget = forms.FileField()
        self.fields["image"].widget = forms.FileField()