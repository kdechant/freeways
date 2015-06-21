from django.db import models
from geopy.distance import vincenty
import json

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=200)
    lane_miles = models.IntegerField(default=0)
        
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'cities'
    
    # calculate statistics and routes for a city
    def getRoutes(self):
        all_routes = RouteSegment.objects.order_by('distance_from_origin', '-lane_miles')
        remaining_lane_miles = self.lane_miles
        active_routes = []
        for route in all_routes:
            route_lane_miles = route.length * route.lanes;
            # check if we have enough lane miles left to add this route segment 
            if remaining_lane_miles > route_lane_miles:
                active_routes.append(json.loads(route.geojson))
                remaining_lane_miles -= route_lane_miles

        output = {'name': self.name, 'lane_miles': self.lane_miles, 'remaining_lane_miles': str(remaining_lane_miles), 'routes': active_routes}
        return output
    
class RouteSegment(models.Model):
    highway = models.CharField(max_length=200)
    segment_name = models.CharField(max_length=200)
    distance_from_origin = models.DecimalField(default=0, max_digits=6, decimal_places=3, editable=False)
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

        # calculate lane miles based on segment length
        self.lane_miles = self.length * self.lanes

        # use geopy to calculate the distance from the origin point (downtown)
        downtown = (34.052234, -118.243685)
        start_point = [self.start_lat, self.start_lng]
        end_point = [self.end_lat, self.end_lng]
        distance1 = vincenty(downtown, start_point).miles
        distance2 = vincenty(downtown, end_point).miles
        self.distance_from_origin = min(distance1, distance2)

        super(RouteSegment, self).save()
