from django.contrib import admin
# from .models import related models
from .models import CarMake, CarModel

# Register your models here.
class CarModelInline(admin.StackedInline):
    model = CarModel 
    extra = 2
class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
admin.site.register(CarMake)
admin.site.register(CarModel)
# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
