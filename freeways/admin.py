from django.contrib import admin

# Register your models here.
from .models import City
from .models import RouteSegment

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'lane_miles')

class RouteSegmentAdmin(admin.ModelAdmin):
    list_display = ('highway', 'segment_name', 'ring', 'length', 'lane_miles')
    list_filter = ['ring']

admin.site.register(RouteSegment, RouteSegmentAdmin)
admin.site.register(City, CityAdmin)
