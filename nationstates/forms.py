from django import forms
from nationstates.models import State
class NationForm(forms.ModelForm):
    
    name = forms.CharField(label='Country Name', max_length=)
    
    class Meta:
        model = State
        fields = ('name', 'description', 'motto', 'animal', 'currency')

class IssueForm(forms.Form):
    def __init__(self, issue, *args, **kwargs):
        choices = [(solution.id, solution) for solution in issue.solutions]
        self.fields['solutions'] = ChoiceField(
            required=True, 
            choices=choices, 
            widget=RadioSelect())
        super(IssueForm, self).__init__(*args, **kwargs)
    