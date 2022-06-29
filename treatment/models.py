from django.db import models
from django.urls import reverse

TREATMENTS = ((0, "Facial"), (1, "Make-Up"), (2, "Pedicure"), (3, "Manicure"), (4, "Hair Styling"))

class Treatment(models.Model):
    treatment_type = models.IntegerField(choices=TREATMENTS)
    treatment_name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=60, unique=True, primary_key=True)
    treatment_price = models.DecimalField(blank=False, max_digits=5, decimal_places=2)
    treatment_description = models.TextField()
    treatment_time = models.CharField(max_length=50)

    class _Meta:
        ordering = ['treatment_name']
    
    def __str__(self):
        return f"{self.treatment_name}"
    
    def __name__(self):
        return f" Treatment: {self.treatment_name}"

    def get_absolute_url(self):
        return reverse("treatment-price/", kwargs={"slug": self.slug})
    