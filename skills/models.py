from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField(upload_to='skills/')  # Make sure MEDIA settings are configured
    acquired_from = models.CharField(max_length=200)  # Where you acquired the skill

    def __str__(self):
        return self.name
