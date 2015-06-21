from django.contrib import admin

# Register your models here.
from .models import City
from .models import RouteSegment

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'lane_miles')

class RouteSegmentAdmin(admin.ModelAdmin):
    list_display = ('highway', 'segment_name', 'distance_from_origin', 'length', 'lane_miles')
    list_filter = ['highway']

admin.site.register(RouteSegment, RouteSegmentAdmin)
admin.site.register(City, CityAdmin)
