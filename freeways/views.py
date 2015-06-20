from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

from .models import RouteSegment, City

# Create your views here.
def index(request):
    cities = City.objects.all()
    return render(request, 'index.html', {'cities': cities})

# API method to provide stats and route data for a city. Outputs JSON.
def api(request, city_id):
    return HttpResponse(json.dumps('Under construction'), content_type="application/json")
