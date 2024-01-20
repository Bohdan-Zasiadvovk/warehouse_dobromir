from django.db import models


class Item(models.Model):

    CATEGORY_CHOICES = [
        ('ingredient', 'Інгредієнт'),
        ('additional_product', 'Додаткові продукти'),
        ('package', 'Пакети'),
        ('label', 'Етикетки'),
        ('crouton', 'Сухарики'),
        ('box', 'Ящики'),
    ]

    MEASURE_CHOICES = [
        ('kilogram', 'кілограм'),
        ('meter', 'метри'),
        ('piece', 'штук')
    ]

    name = models.CharField(max_length=50)
    measure = models.CharField(max_length=20, choices=MEASURE_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.name} - {self.measure} ({self.category})"
