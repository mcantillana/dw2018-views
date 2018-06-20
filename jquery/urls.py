from django.urls import path
from jquery import views


urlpatterns = [
    path('', views.index, name="index"),
    path('show', views.show, name="show"),
    path('show/json', views.json, name="show_json"),

]
