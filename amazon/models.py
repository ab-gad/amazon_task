from django.db import models

# Create your models here.

class myUsers(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=20)


class Track(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

class Intake(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=3)

class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, unique=True)
    track_id = models.ForeignKey(Track, on_delete=models.CASCADE)
    intake_id = models.ForeignKey(Intake, on_delete=models.CASCADE)


