from django.db import models
from datetime import datetime, timedelta, date


# Create your models here.
class Factory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Firma'
        verbose_name_plural = 'Firmalar'
        

class Drug(models.Model):
    title = models.CharField(max_length=100)
    factory = models.ForeignKey(Factory, on_delete=models.SET_NULL, null=True)
    price = models.FloatField()
    expirate = models.DateField()
    recipe_needed = models.BooleanField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Derman'
        verbose_name_plural = 'Dermanlar'

    def expired(self):
        return self.expirate < date.today()

    def get_expire_info(self):
        if self.expirate < (date.today() - timedelta(days=10)):
            return 'Vaxti Kecib'
        elif self.expirate < date.today():
            return 'Vaxtina Az qalib'
        else:
            return 'Hele Var'

    def save(self, *args, **kwargs):
        self.title = self.title.upper()
        super().save(*args, **kwargs)
