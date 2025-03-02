from django.db import models


class ImageSetting(models.Model):
    id = models.CharField(max_length=40, primary_key=True,unique=True)
    image = models.ImageField(upload_to='images/')

    # common fields
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id