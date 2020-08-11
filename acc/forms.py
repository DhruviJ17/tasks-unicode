from django.forms import ModelForm

from .models import *

class NumForm(ModelForm):
    class Meta:
        model = Num
        fields = '__all__'
