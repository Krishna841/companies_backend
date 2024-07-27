from django.db import models

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    entity = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    email = models.EmailField()
    incorporation = models.DateField()
    address = models.TextField()
    revenue = models.DecimalField(max_digits=10, decimal_places=2)
    website = models.URLField()
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.entity
