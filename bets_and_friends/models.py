from django.db import models

# Create your models here.
# class Tournament(models.Model):
# 	title = models.CharField(max_length=120)
# 	description = models.TextField(blank=True, null=True) # null=True -> it's ok for them to be null in the DB
# 														  # blank=True -> the value can be empty
# 	price = models.DecimalField(decimalPlaces=2, max_digits=1000)
# 	isFeatured = models.BooleanField(default=True)