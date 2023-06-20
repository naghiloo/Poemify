from django.db import models

from base.models import BaseModel
from poetry.models import Category


class Status(BaseModel):
    code = models.IntegerField()
    description = models.CharField(max_length=64, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='statuses')

    class Meta:
        db_table = 'statuses'

    def __str__(self):
        return str(self.code)