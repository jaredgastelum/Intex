from django.db import models

# Create your models here.
from datetime import datetime


class Person(models.Model):
    personid = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)
    phone = models.CharField(max_length=14)
    email = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    #main_photo = models.ImageField(upload_to='photos', null=True)
    morbidities = models.ManyToManyField('Morbidity')

    def __str__(self):
        return (self.first_name + ' ' + self.last_name)


class Morbidity(models.Model):
    morbidityID = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    datediagnosed = models.DateTimeField(default=datetime.today, blank=True)

    def __str__(self):
        return (self.name)


class LabVitals(models.Model):
    vitalid = models.BigAutoField(primary_key=True)
    personID = models.ForeignKey(
        Person, null=True, blank=True, on_delete=models.SET_NULL)
    K = models.DecimalField(max_digits=5, decimal_places=2)
    Phos = models.DecimalField(max_digits=5, decimal_places=2)
    Na = models.DecimalField(max_digits=5, decimal_places=2)


    Creatinine = models.DecimalField(max_digits=5, decimal_places=2, default=0)




    Albumin = models.DecimalField(max_digits=5, decimal_places=2)
    BloodSugar = models.IntegerField(default=0)
    BloodPressure = models.CharField(max_length=10)
    Weight = models.DecimalField(max_digits=5, decimal_places=2)
    Date = models.DateTimeField(default=datetime.today, blank=True)

    def __str__(self):
        return (self.vitalid)


class Food(models.Model):
    foodID = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    
    sodium = models.DecimalField(max_digits=5, decimal_places=2)
    protein = models.DecimalField(max_digits=5, decimal_places=2)
    k = models.DecimalField(max_digits=5, decimal_places=2)
    phosphorus = models.DecimalField(max_digits=5, decimal_places=2)
    sugar = models.IntegerField(default=0)
    cholesterol = models.DecimalField(max_digits=5, decimal_places=2)
    water = models.IntegerField(default=0)
    

    def __str__(self):
        return (self.name)


class FoodEntry(models.Model):
    foodentryid = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(default=datetime.today, blank=True)
    mealType = models.CharField(max_length=20)
    personID = models.ForeignKey(
        Person, null=True, blank=True, on_delete=models.SET_NULL)
    foods = models.ManyToManyField(Food, through='Serving', blank=True)

    def __str__(self):
        return (self.mealType)


class Serving(models.Model):
    class Meta:
        unique_together = [('foodID', 'foodentryID')]
    foodID = models.ForeignKey(Food, on_delete=models.CASCADE)
    foodentryID = models.ForeignKey(FoodEntry, on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=5, decimal_places=2)
    kind = models.CharField(max_length=20)

    def __str__(self):
        return (self.amount)


class JournalEntry(models.Model):
    entryID = models.BigAutoField(primary_key=True)
    personID = models.ForeignKey(
        Person, null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(default=datetime.today, blank=True)
    notes = models.CharField(max_length=3000)
    status = models.CharField(max_length=25)

    def __str__(self):
        return (self.status)


class ExerciseEntry(models.Model):
    exerciseID = models.BigAutoField(primary_key=True)
    personID = models.ForeignKey(
        Person, null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(default=datetime.today, blank=True)
    duration = models.IntegerField
    weight = models.IntegerField

    def __str__(self):
        return (self.duration)

class DailyTotal(models.Model):
    dailytotalid = models.BigAutoField(primary_key=True)
    date = models.DateField(default=date.today, blank=True)

    sodium = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    protein = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    k = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    phosphorus = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    sugar = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    cholesterol = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    water = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return (str(self.date))

