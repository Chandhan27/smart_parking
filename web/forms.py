# parking/forms.py
from django import forms

class HelpForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Email')
    issue = forms.CharField(widget=forms.Textarea, label='Describe Your Issue')
