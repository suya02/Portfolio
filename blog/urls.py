from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('aboutMe', views.aboutMe, name='aboutMe'),
    path('Portfolio', views.Portfolio, name='Portfolio'),
    path('Contact', views.Contact, name='Contact'),
]