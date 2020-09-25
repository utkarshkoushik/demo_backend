from django.db import models

class userData(models.Model):
    GENDER_MALE = 'Male'
    GENDER_FEMALE = 'Female'
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    name = models.CharField(max_length = 500)
    photo = models.FileField()
    email = models.EmailField(max_length = 300, unique =True)
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    pathname = models.CharField(max_length = 100, primary_key=True)