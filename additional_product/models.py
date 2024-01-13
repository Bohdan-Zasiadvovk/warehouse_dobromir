from django.db import models


class AdditionalProduct(models.Model):
    name = models.CharField(max_length=50)
    measure = models.CharField(max_length=20)

    def __str__(self):
        return self.name
