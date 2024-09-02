from django.db import models

# Create your models here.


class Genre(models.Model):
    genres_name = models.CharField(max_length=150, null=True)
    
    def __str__(self):
        return self.genres_name

class Movie_Details(models.Model):
    genre_name = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    movie_name= models.CharField(max_length=150, null=True)  
    image = models.ImageField(upload_to='images/',null=True)

    director = models.CharField(max_length=150, null=True) 
    production_company =models.CharField(max_length=150, null=True)
    actors=models.CharField(max_length=150, null=True)
    details=models.CharField(max_length=500, null=True)


    def __str__(self):
        return self.movie_name