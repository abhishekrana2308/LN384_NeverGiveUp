from django.contrib import admin
from .models import Person, Sector, Board, Notification, Table,Alert
# Register your models here.

admin.site.register(Person)
admin.site.register(Sector)
admin.site.register(Board)
admin.site.register(Notification)
admin.site.register(Table)
admin.site.register(Alert)