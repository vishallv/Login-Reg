from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^registeruser$',views.registerUser),
    url(r'^loginuser$',views.loginUser),
    url(r'^success$',views.success),
    url(r'^destroy$',views.destroy),
    
]