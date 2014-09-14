import datetime, os
from django.conf import settings
from django.core import urlresolvers
from django.contrib.sitemaps import Sitemap


class StaticSitemap(Sitemap):
    """Return the static sitemap items"""
    priority = 0.5

    def __init__(self, urls):
        self._items = urls

    def items(self):
        return self._items

    def changefreq(self, obj):
        return 'monthly'

    def lastmod(self, obj):
        return datetime.datetime.now()

    def location(self, obj):
        return obj
