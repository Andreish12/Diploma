app_name = 'contact'

from django.urls import path
from .views import contact_seller



urlpatterns = [
    path('<int:listing_id>/', contact_seller, name='contact_seller'),
    
]
