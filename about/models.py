from django.db import models


class Education(models.Model):
    institution = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-start_year']

    def __str__(self):
        return f"{self.course} - {self.institution}"


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    client_name = models.CharField(max_length=200)
    client_photo = models.ImageField(
        upload_to='testimonials/',
        null=True,
        blank=True
    )
    content = models.TextField()
    service = models.ForeignKey(
        Service,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    contact_info = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Testimonial by {self.client_name}"
