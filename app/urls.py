from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
     path('hello/',views.hello),
     path('talk/',views.talk),
     path('my_webhook/',views.my_webhook),

]

