from django.db import models

# Create your models here.
class WorkExperience(models.Model):
    company_photo = models.ImageField(upload_to='company_photos/' ,blank=True, null=True)
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.position} at {self.company_name}"
    
    