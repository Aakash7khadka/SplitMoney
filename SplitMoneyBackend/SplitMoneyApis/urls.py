from django.urls import path, include
from . import views
urlpatterns = [

    path('alltrips', views.get_all_trips),
    path('add_trip/', views.insert_trip),
    path('add_trip_participants/', views.insert_trip_participants),
    path('add_expenses/', views.insert_expenses),
]