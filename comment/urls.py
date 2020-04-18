from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index$',views.index),
    url(r'^addData$',views.addData),
    url(r'^getData$',views.getData)
]