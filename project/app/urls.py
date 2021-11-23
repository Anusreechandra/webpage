from os import name
from django.urls import path
from django.urls.resolvers import URLPattern
from. import views
app_name="app"
urlpatterns=[
    path('',views.new,name="web"),

]