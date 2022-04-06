import operator

from functools import reduce

import django_filters
from django.db.models import Q
from django.contrib.gis.geos import fromstr, Point, GEOSGeometry
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Distance
from django.conf import settings

from core.models import VirtualShop


class VirtualShopListFilter(django_filters.FilterSet):
    lat_long = django_filters.CharFilter(method='get_closest_virtualshops')
    filter = django_filters.CharFilter(method='search_virtualshops_by_name')

    class Meta:
        model = VirtualShop
        fields = ['lat_long', 'filter', 'foodItems__title', 'virtualShopCategory__title']

    def get_closest_virtualshops(self, queryset, name, value):
        latitude, longitude = value.split(",")
        user_location = fromstr(f'POINT({latitude} {longitude})', srid=4326)

        return queryset.filter(
            address__location__distance_lte=(
                user_location, D(m=settings.MAXIMUM_MILES_DISTANCE))
        ).annotate(
            distance=Distance("address__location", user_location)
        ).order_by("distance")

    def search_virtualshops_by_name(self, queryset, name, value):
        filters = value.split("&")
        conditions = []

        for filter in filters:
            name, value = filter.split("=")
            dict_filter = {
                '{}__icontains'.format(name): value
            }
            conditions.append(Q(**dict_filter))

        if conditions:
            return queryset.filter(reduce(operator.or_, conditions)).distinct()

        return queryset

