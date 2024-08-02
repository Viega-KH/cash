from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class news(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    image = models.ImageField(upload_to='news/')
    category = models.ForeignKey(category, on_delete=models.CASCADE, related_name='news')
    published_date = models.DateField(auto_now_add=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
