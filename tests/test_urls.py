from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib import admin

from markers.views import MarkersMapView


class TestUrls(SimpleTestCase):
    """ Test class for URLs """

    # collect the URLs as hashmaps
    urlpatterns = []
    up = {"url": "admin", "func": admin.site.urls, "name": "admin"}
    urlpatterns.append(up)
    up = {"url": "map", "func": MarkersMapView, "name": "markers"}
    urlpatterns.append(up)
    #path("markers/", include("markers.urls")),
    #    path("map/", MarkersMapView.as_view(), name="markers"),

    def test_url0(self):
        up = self.urlpatterns[0]
        url = reverse(viewname = up["name"])
        self.assertEqual(resolve(url).func, up["func"])

    def test_url1(self):
        up = self.urlpatterns[1]
        url = reverse(viewname = up["name"])
        self.assertEqual(resolve(url).func.view_class, up["func"])

