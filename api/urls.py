from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path("", views.home),
   path("items/", views.fetch_items),
   path("items/insert/", views.insert_items),
   path("items/update/<int:id>", views.update_items),
   path("items/delete/<int:id>", views.delete_items),
]
