from django.db import models

class Player(models.Model):
    file = models.FileField(upload_to='')
    