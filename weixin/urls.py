from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^alltoutiao/', views.index),
    url(r'^add/', views.add),
]
