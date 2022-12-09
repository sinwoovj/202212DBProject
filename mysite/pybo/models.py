from django.db import models

# Create your models here.

class Designer(models.Model) :
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    name = models.CharField(max_length=50)
    adress =models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self) :
        return self.name