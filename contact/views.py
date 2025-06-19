from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from listings.models import Listing
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages








def contact_seller(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            user_name = form.cleaned_data['name']
            user_phone = form.cleaned_data['phone']
            user_message = form.cleaned_data['message']

            subject = f"Интерес к объявлению: {listing.title}"
            message = (
                f"Пользователь {user_name} ({user_email}, тел: {user_phone}) "
                f"заинтересован в вашем объявлении.\n\n"
                f"Ссылка: {settings.SITE_URL}/listing/{listing.id}/\n\n"
                f"Сообщение:\n{user_message}"
            )

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [listing.author.email],
                fail_silently=False,
            )

           
            messages.success(request, "Сообщение успешно отправлено продавцу.")
            return redirect('listing_detail', pk=listing.id)

    else:
        form = ContactForm(initial={
            'email': request.user.email,
            'name': request.user.username,
        })

    return render(request, 'contact/contact_form.html', {'form': form, 'listing': listing})
