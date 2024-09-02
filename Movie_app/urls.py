from django.urls import path

from Movie_app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('details/<int:id>',views.detail_view,name='details'),
    path('genres_view/<int:id>',views.genres_view,name='genres_view')


]


