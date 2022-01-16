from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name="main"),
    path('kpop/', views.kpop, name="kpop"),
    path('kpop/<int:id>', views.idol, name="idol"),
    path('add-idol/', views.add_idol, name="add_idol")
]