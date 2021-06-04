from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='', null=True,
                              default="")
    sku = models.CharField(max_length=10)

    def __str__(self):
        return self.name + " " + self.sku

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
