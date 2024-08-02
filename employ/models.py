from django.db import models

class department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class leadership(models.Model):
    full_name = models.CharField(max_length=200)
    department = models.ForeignKey(department, on_delete=models.CASCADE, related_name='leaders')
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    acceptance = models.CharField(max_length=100, )
    image = models.ImageField(upload_to='leadership/')
    published_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name}"
