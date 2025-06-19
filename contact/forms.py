from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(required=False)
    phone = forms.CharField(max_length=20, required=False)
    message = forms.CharField(widget=forms.Textarea)
