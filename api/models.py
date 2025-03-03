from django.db import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=150, unique=True, null=False)
    localisation = models.CharField(max_length=255, null=True, blank=True)

class Zones(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100, null=False)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
    type_de_sol = models.CharField(max_length=100, null=True, blank=True)
    climat = models.JSONField(null=True, blank=True)

class Plantes(models.Model):
    id = models.AutoField(primary_key=True)
    nom_commun = models.CharField(max_length=100, null=False)
    nom_scientifique = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    saison_culture = models.CharField(max_length=50, null=True, blank=True)
    image_url = models.CharField(max_length=200, null=True, blank=True)

class Diagnostics(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True) 
    image_url = models.CharField(max_length=200, null=False)
    resultat = models.CharField(max_length=100, null=False)
    conseils = models.TextField(null=True, blank=True)
    plante = models.ForeignKey(Plantes, related_name="diagnostics", on_delete=models.CASCADE)
    user = models.ForeignKey(Users, related_name="diagnostics", on_delete=models.CASCADE)

class Recommandations(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)
    dosage = models.CharField(max_length=100, null=True, blank=True)
    periode_utilisation = models.CharField(max_length=100, null=True, blank=True)
    zone = models.ForeignKey(Zones, related_name="recommandations", on_delete=models.SET_NULL, null=True, blank=True)
    plante = models.ForeignKey(Plantes, related_name="recommandations", on_delete=models.SET_NULL, null=True, blank=True)
