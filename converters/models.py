from django.db import models

class Document(models.Model):
    converted_text = models.TextField(blank=True)
    converted = models.BooleanField(default=False)
