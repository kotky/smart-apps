from django.contrib.postgres.fields import JSONField
from django.db import models

class UniversalJsonContainer(models.Model):
    session_id = models.PositiveIntegerField(default=0, null=False, blank=False)
    content_type = models.CharField(max_length=64, default="data", null=False, blank=False)
    data = JSONField()
