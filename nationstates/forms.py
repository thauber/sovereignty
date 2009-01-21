from django import forms
from nationstates.models import State
class NationForm(forms.ModelForm):
    
    name = forms.CharField(label='Country Name', max_length=)
    
    class Meta:
        model = State
        fields = ('name', 'description', 'motto', 'animal', 'currency')