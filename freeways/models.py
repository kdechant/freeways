from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=200)
    lane_miles = models.IntegerField(default=0)
        
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'cities'
    
class RouteSegment(models.Model):
    highway = models.CharField(max_length=200)
    segment_name = models.CharField(max_length=200)
    ring = models.IntegerField(default=1)
    length = models.DecimalField(default=0, max_digits=5, decimal_places=2, blank=True)
    lanes = models.IntegerField(default=10)
    lane_miles = models.DecimalField(default=0, max_digits=5, decimal_places=2, blank=True)
    start_lat = models.DecimalField(max_digits=10, decimal_places=6)
    start_lng = models.DecimalField(max_digits=10, decimal_places=6)
    end_lat = models.DecimalField(max_digits=10, decimal_places=6)
    end_lng = models.DecimalField(max_digits=10, decimal_places=6)
    geojson = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.highway + " - " + self.segment_name
    
