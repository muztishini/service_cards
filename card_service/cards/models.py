from django.db import models


class Card(models.Model):
    seria = models.IntegerField()
    nomer = models.BigIntegerField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    summa = models.IntegerField()
    srok = models.CharField(max_length=255)
    status = models.CharField(max_length=255)


class Info(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    change = models.CharField(max_length=255)
    value = models.IntegerField()
