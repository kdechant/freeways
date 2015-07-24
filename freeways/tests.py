from django.test import TestCase

from .models import City, RouteSegment

class CityTests(TestCase):
    fixtures = ['freeways/fixtures/freeways.json',]
    def testToString(self):
        c = City(name='Portland')
        self.assertEqual(str(c), 'Portland')
        
    def testRouteSelection(self):
        # city 1
        c = City.objects.get(pk=1)
        routes = c.getRoutes()
        self.assertEqual(routes['name'], str(c))
        self.assertEqual(routes['lane_miles'], c.lane_miles)
        self.assertEqual(len(routes['routes']), 3)
        self.assertEqual([{"rt":1},{"rt":2},{"rt":5}], routes['routes'])

        c = City.objects.get(pk=2)
        routes = c.getRoutes()
        self.assertEqual([{"rt":1},{"rt":2},{"rt":3},{"rt":4}], routes['routes'])

class RouteSegmentModelTests(TestCase):
    def testToString(self):
        r = RouteSegment(highway='5', segment_name='405 to 84')
        self.assertEqual(str(r), '5 - 405 to 84')
        