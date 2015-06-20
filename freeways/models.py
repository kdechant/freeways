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
    length = models.DecimalField(default=0, max_digits=5, decimal_places=2, editable=False)
    lanes = models.IntegerField(default=10)
    lane_miles = models.DecimalField(default=0, max_digits=5, decimal_places=2, editable=False)
    start_lat = models.DecimalField(max_digits=10, decimal_places=6)
    start_lng = models.DecimalField(max_digits=10, decimal_places=6)
    end_lat = models.DecimalField(max_digits=10, decimal_places=6)
    end_lng = models.DecimalField(max_digits=10, decimal_places=6)
    geojson = models.TextField(null=True, blank=True, editable=False)
    
    def __str__(self):
        return self.highway + " - " + self.segment_name
    
    def save(self):
        # get the geoJSON and route length from the yournavigation API
        import urllib.request
        import json
        url = 'http://www.yournavigation.org/api/1.0/gosmore.php?format=geojson&flat={0:f}&flon={1:f}&tlat={2:f}&tlon={3:f}&v=motorcar'.format(self.start_lat, self.start_lng, self.end_lat, self.end_lng)
        with urllib.request.urlopen(url) as response:
           jsonString = response.read().decode(encoding='UTF-8')
        jsonDict = json.loads(jsonString)
        self.length = float(jsonDict['properties']['distance'])
        self.geojson = jsonString
        self.lane_miles = self.length * self.lanes
        super(RouteSegment, self).save()
