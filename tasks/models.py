from django.db import models

# Create your models here.


class Tasks(models.Model):
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    nlevel = models.CharField(max_length=1, blank=True, null=True)
    review = models.BooleanField(blank=True, null=True)
    pricebook = models.TextField(blank=True, null=True)
    datepublic = models.DateField(blank=True, null=True)
    datesell = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tasks'

"""

- Bibliografia:

https://docs.djangoproject.com/en/5.0/ref/models/fields/

"""