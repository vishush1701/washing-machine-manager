from django.contrib import admin
from .models import WashingMachine
from .models import User
from .models import Location

# Register your models here.

admin.site.register(WashingMachine)
admin.site.register(User)
admin.site.register(Location)
