from models import Strategy
from django.forms import ModelForm
from django.forms.widgets import Textarea,TextInput
class StrategyForm(ModelForm):

    class Meta:
        model=Strategy
        fields = ['user','title','description','code','status']
        widget={
            'code': Textarea(attrs={"width": "100%","height":"500px"}),
            'user': TextInput(attrs={'class': "form-control"}),
            'title': TextInput(attrs={'class': "form-control"}),
            'description': TextInput(attrs={'class': "form-control"}),
        }