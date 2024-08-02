from django.db import models


class contact(models.Model):
    full_name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    # email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    published_date = models.DateField(auto_now_add=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.phone}"
