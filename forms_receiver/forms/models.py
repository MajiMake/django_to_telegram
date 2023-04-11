from django.db import models


class Form(models.Model):
    name: str = models.CharField(max_length=20)

