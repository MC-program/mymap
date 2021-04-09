import json

from django.contrib.gis.gdal import OGRGeometry
from django.shortcuts import render
from django.core.serializers import serialize
from django.views.generic.base import TemplateView

from django.contrib.gis.gdal import OGRGeometry

from .models import Marker


class MarkersMapView(TemplateView):
    """Markers map view."""

    template_name = "map.html"

    def get_context_data(self, **kwargs):
        """Return the view context data."""
        context = super().get_context_data(**kwargs)
        #print("context", context)
        context["markers"] = json.loads(serialize("geojson", Marker.objects.all()))
        #print("context[markers]", context["markers"])
        """
        "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    14.08591836494682,
                    42.08632592463349
                ]
            }
        }
        ]
        features = {}
        features["type"] = "Feature"
        geometry = {}
        geometry["type"] = "Point"
        geometry["coordinates"] = [14, 11]
        features["geometry"] = geometry  #OGRGeometry('POINT(1 2)')
        context["markers"]["features"] = features
        print("context[markers]", context["markers"])
        """
        return context


