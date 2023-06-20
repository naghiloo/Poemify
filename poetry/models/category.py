from django.db import models

from base.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=64)
    symbol = models.CharField(max_length=3)
    description = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        db_table = 'categories'
