from django.forms import ModelForm

from .models import *

class NumForm(ModelForm):
    class Meta:
        model = Num
        fields = '__all__'

class parsedData(ModelForm):
    class Meta:
        model = ApiQuery
        fields = ['username']

class RepoData(ModelForm):
    class Meta:
        model = ApiQuery
        fields = ['repo_count']

class FoloData(ModelForm):
    class Meta:
        model = ApiQuery
        fields = ['followers_count']
