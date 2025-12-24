from django.db import models

# Create your models here.
class CV(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='cvs/')
    def __str__(self):
        return self.name