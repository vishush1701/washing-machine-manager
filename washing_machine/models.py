from django.db import models

# Create your models here.
class Location(models.Model):
    floor = models.CharField(max_length=4)
    room = models.CharField(max_length=3)
    building_name = models.CharField(max_length=25)

    def __str__(self):
        return f'building:{self.building_name} floor:{self.floor} room:{self.room}'

class User(models.Model):
    name = models.CharField(max_length=15)
    location = models.ForeignKey(Location,related_name="location",null=True,on_delete=models.SET_NULL)
    email = models.CharField(max_length=25,null=True)

    def __str__(self):
        return f'name:{self.name} location:{self.location}'

class WashingMachine(models.Model):
    name = models.CharField(max_length=20)
    is_available = models.BooleanField(default=True)
    using_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    location = models.OneToOneField(Location,related_name="wm_location",on_delete=models.SET_NULL,null=True)
    
    def __str__(self) -> str:
        return f'washing machine:{self.name} location:{self.location.floor}'
    
    class Meta:
        constraints = [models.UniqueConstraint(fields=['name'],name="unique_washing_machine")]
