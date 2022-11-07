from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', welcome),
    path('about_us/', about),
    path('date_now/', date_),
    path('films/', films),
    path('directors/', directors),
    path('films/<int:id>/', one_film),
    path('director/<int:director_id>/films/', director_films),
    path('films/create/', create_film),
    path('director/create/', create_director),
    path('register/', register_),
    path('login/', login_),
    path('logout/', logout_),
    path('search/', search)
]
