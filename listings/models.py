from django.db import models
from users.models import CustomUser
from django.core.validators import MinValueValidator

class Listing(models.Model):
    STATUS_CHOICES = [
        ('active', 'Активное'),
        ('sold', 'Продано'),
        ('deleted', 'Удалено'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(
    validators=[MinValueValidator(0)],
    verbose_name="Цена (в рублях)")
    city = models.CharField(max_length=100)
    image = models.ImageField(upload_to='listing_images/')
    pdf_file = models.FileField(upload_to='listing_pdfs/', blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='listings')

    def __str__(self):
        return self.title
