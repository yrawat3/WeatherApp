from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name = 'index') #homepage, from views file go to the index function, name given to the url 
]