from django.contrib import admin

# Register your models here.
from .models import Student
from .models import Stdent
from .models import Room

admin.site.register(Student)
admin.site.register(Stdent)
admin.site.register(Room)
