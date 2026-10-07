from django.contrib import admin

from myapp.models import People ,MyModel

# Register your models here.
@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone_number", "joined_date")

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ("name", "description")