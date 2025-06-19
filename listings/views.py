from django.shortcuts import redirect, render, get_object_or_404
from .models import Listing
from contact.forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from .forms import ListingForm
from .models import Listing
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Listing

class ListingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Listing
    template_name = 'listings/delete_listing.html'
    success_url = reverse_lazy('my_listings')

    def test_func(self):
        return self.get_object().author == self.request.user


class MyListingsView(LoginRequiredMixin, ListView):
    model = Listing
    template_name = 'listings/my_listings.html'
    context_object_name = 'listings'

    def get_queryset(self):
        return Listing.objects.filter(author=self.request.user)
    

@method_decorator(login_required, name='dispatch')
class ListingCreateView(CreateView):
    model = Listing
    form_class = ListingForm
    template_name = 'listings/create_listing.html'
    success_url = reverse_lazy('home')  # на главную после создания

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
    
def listing_list(request):
    listings = Listing.objects.filter(status='active').order_by('-date_posted')
    return render(request, 'listings/listing_list.html', {'listings': listings})


def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    sent = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            subject = f'Интерес к объявлению: {listing.title}'
            message = (
                f"Имя: {data.get('name')}\n"
                f"Email: {data.get('email')}\n"
                f"Телефон: {data.get('phone')}\n\n"
                f"Сообщение:\n{data.get('message')}\n\n"
                f"Ссылка на объявление: {settings.SITE_URL}/listing/{listing.id}/"
            )
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [listing.author.email],
            )
            sent = True
    else:
        initial = {}
        if request.user.is_authenticated:
            initial = {
                'name': request.user.username,
                'email': request.user.email,
                'phone': request.user.phone,
            }
        form = ContactForm(initial=initial)

    return render(request, 'listings/listing_detail.html', {
        'listing': listing,
        'form': form,
        'sent': sent,
    })
    
    
def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.author = request.user
            listing.save()
            return redirect('my_listings')
    else:
        form = ListingForm()
    return render(request, 'listings/create_listing.html', {'form': form})
   
    
def listing_list(request):
    listings = Listing.objects.filter(status='active')

    city = request.GET.get('city')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    query = request.GET.get('q')

    if city:
        listings = listings.filter(city__icontains=city)
    if min_price:
        listings = listings.filter(price__gte=min_price)
    if max_price:
        listings = listings.filter(price__lte=max_price)
    if query:
        listings = listings.filter(title__icontains=query)

    return render(request, 'listings/listing_list.html', {
        'listings': listings,
        'filters': {
            'city': city or '',
            'min_price': min_price or '',
            'max_price': max_price or '',
            'q': query or '',
        }
    })    
    
    
    
    