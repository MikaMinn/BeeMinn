from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
    
class Zones(models.Model):
    name = models.CharField('nom', max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField('ville', max_length=100)
    zip_code = models.IntegerField('code_postal')

    class Meta:
        verbose_name = "Zone"

    def __str__(self):
        return self.name

class Hives(models.Model):
    name = models.CharField('nom', max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField('date de création', auto_now_add=True)
    year = models.IntegerField('Année de la reine', default=2020)
    origin = models.CharField('origine', max_length=100, default="Eleveur")
    zone = models.ForeignKey(Zones, on_delete=models.CASCADE)
    type = [
        ('Dadant' , 'Dadant'),
        ('Langstroth' , 'Langstroth'),
        ('Warré' , 'Warré')
    ]
    hive_type = models.CharField('nom du type de ruche', max_length=100, choices=type)
    frame_number = models.IntegerField('nombre de cadre', default="10")
    description = models.TextField('description', max_length=500, blank=True)
    class Meta:
        verbose_name = "ruche"

    def __str__(self):
        return self.name

class History(models.Model):
    created_at = models.DateTimeField('date de création', default=datetime.now)
    details = models.TextField('détails', max_length=1000)
    hive = models.ForeignKey(Hives, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Historique"
