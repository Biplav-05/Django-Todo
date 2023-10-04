from django import forms
from .models import Todo

class TodoForm(forms.Form):
    text = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control me-1'}))

class NewTodoForm(forms.ModelForm): 
    class Meta:
         model =  Todo
         fields =  ['text']
         widgets = {
             'text': forms.TextInput(
                 attrs={'class':'form-control me-1'})
         }