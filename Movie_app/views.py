from django.shortcuts import render

from Movie_app.models import Genre, Movie_Details

# Create your views here.
def home(request):
    ca=Genre.objects.all()
    movie=Movie_Details.objects.all()
    return render(request,'movie.html',{'movie':movie,'ca':ca})


def genres_view(request,id):
    ca=Genre.objects.get(id=id)

    movie=Movie_Details.objects.filter(genre_name=ca)
    return render(request,'movie.html',{'movie':movie})


def detail_view(request,id):
    ca=Genre.objects.all()

    details=Movie_Details.objects.get(id=id)
    return render(request,'details.html',{'details':details,'ca':ca})