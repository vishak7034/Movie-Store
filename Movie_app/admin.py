from django.contrib import admin

from Movie_app.models import Genre, Movie_Details

# Register your models here.
admin.site.register(Genre)
admin.site.register(Movie_Details)
