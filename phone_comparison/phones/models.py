from django.db import models


class Phone(models.Model):
    model = models.CharField(max_length=200)
    price = models.IntegerField()
    os = models.CharField(max_length=200)
    screen_resolution = models.CharField(max_length=200)
    camera_resolution = models.CharField(max_length=200)
    ram = models.IntegerField()
    cpu = models.CharField(max_length=200)


class ApplePhone(Phone):
    air_pods = models.BooleanField()
    face_id = models.BooleanField()
    apple_pay = models.BooleanField()


class SamsungPone(Phone):
    samsung_pay = models.BooleanField()


class PechenkaPhone(Phone):
    fm_radio = models.BooleanField()

