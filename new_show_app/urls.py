from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('shows/new', views.add_show),
    path('shows/create', views.create_show),
    path('shows/<int:number>', views.show_details),
    path('shows', views.shows),
    path('shows/<int:number>/edit', views.edit),
    path('shows/edit/<int:number>', views.make_changes),
    path('shows/<int:number>/destroy', views.delete_show),
]