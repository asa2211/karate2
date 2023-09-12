from datetime import datetime

from django.db import models


class TrenerModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(default=datetime.now)
    image = models.ImageField(upload_to='media/')

    class Meta:
        db_table = 'trener'