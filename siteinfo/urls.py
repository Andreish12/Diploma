app_name = "siteinfo"

from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('about/', TemplateView.as_view(template_name='siteinfo/about.html'), name='about'),
    path('contacts/', TemplateView.as_view(template_name='info/contacts.html'), name='contacts'),
    path('privacy/', TemplateView.as_view(template_name='info/privacy.html'), name='privacy'),
]
