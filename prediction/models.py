from django.db import models


# Create your models here.
class Download(models.Model):
    file_name = models.CharField(max_length=100, default=None)
    file_data = models.FileField(upload_to='uploads/download/', blank=True, null=True)


