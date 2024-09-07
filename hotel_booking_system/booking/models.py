from django.db import models 

class Guests(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    check_in_dates = models.DateField()
    check_out_dates = models.DateField()
    room_number = models.IntegerField(max_length=3)
    type_of_room = models.CharField(max_length=10)
    package_included = models.BooleanField()

def __str__(self):
    return f"{self.first_name} , {self.last_name} , {self.type_of_room}"