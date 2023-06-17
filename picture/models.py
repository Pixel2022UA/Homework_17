from django.db import models


class Picture(models.Model):
    name = models.CharField(max_length=255)
    file = models.ImageField(upload_to="pictures/")

    def __str__(self):
        return self.name
