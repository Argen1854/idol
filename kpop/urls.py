from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name="main"),
    path('kpop/', views.kpop, name="kpop"),
    path('kpop/<int:id>', views.idol, name="idol"),
    path('kpop/<int:id>/update/', views.idol_update, name="idol_update"),
    path('kpop/<int:id>/delete/', views.idol_delete, name="idol_delete"),
    path('add-idol/', views.add_idol, name="add_idol")
]