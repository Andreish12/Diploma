from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'price', 'city', 'image', 'pdf_file']

        labels = {
            'title': 'Название',
            'description': 'Описание',
            'price': 'Цена',
            'city': 'Город',
            'image': 'Изображение',
            'pdf_file': 'PDF файл',}