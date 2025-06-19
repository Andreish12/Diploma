from django.urls import path
from . import views
from .views import listing_list, listing_detail
from .views import MyListingsView, ListingDeleteView, ListingCreateView


urlpatterns = [
    path('', views.listing_list, name='home'),
    #path('', listing_list, name='listing_list'),
    path('listing/<int:pk>/', listing_detail, name='listing_detail'),
    path('create/', ListingCreateView.as_view(), name='create_listing'),
    path('my/', MyListingsView.as_view(), name='my_listings'),
    path('delete/<int:pk>/', ListingDeleteView.as_view(), name='delete_listing'),

]
