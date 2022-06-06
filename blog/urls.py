from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('aboutMe', views.aboutMe, name='aboutMe'),
    path('Portfolio', views.Portfolio, name='Portfolio'),
    path('Contact', views.Contact, name='Contact'),
]