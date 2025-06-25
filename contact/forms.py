from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100, required=False)
    email = forms.EmailField(label='Почта', required=True)
    phone = forms.CharField(label='Телефон', max_length=20, required=False)
    message = forms.CharField(label='Сообщение', widget=forms.Textarea)
