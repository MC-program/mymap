from django.contrib import admin

"""Markers admin.

Register your models here.
"""

from django.contrib.gis import admin
from .models import Marker


@admin.register(Marker)
class MarkerAdmin(admin.OSMGeoAdmin):
    """Marker admin."""

    #list_display = ("name", "location")    # name for marker
    list_display = ("location",)
