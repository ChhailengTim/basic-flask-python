from tastypie.resources import ModelResource
from movies.models import Movie
from django.db import models

class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
        excludes = ['date_created']
        default_format = 'application/json'  # Set JSON as the default format
