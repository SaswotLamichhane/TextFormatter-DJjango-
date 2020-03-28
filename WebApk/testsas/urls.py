from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home),
    path('cap', views.cap, name = 'caption'),
    path('analyze', views.analyze, name = 'analyze')
]
