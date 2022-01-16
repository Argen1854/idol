
from django import forms
from . import models

class IdolForm(forms.ModelForm):
    class Meta:
        model = models.Kpop
        fields = "__all__"