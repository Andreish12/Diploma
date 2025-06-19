from django.contrib import admin
from .models import Listing

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'city', 'status', 'date_posted', 'author')
    list_filter = ('status', 'city', 'date_posted')
    search_fields = ('title', 'description', 'city', 'author__username')
