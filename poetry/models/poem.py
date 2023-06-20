from django.db import models

from base.models import BaseModel
from poetry.models import Status


class Poem(BaseModel):
    parts = models.JSONField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='poems')

    class Meta:
        db_table = 'poems'
