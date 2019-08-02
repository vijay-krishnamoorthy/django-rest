from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('posts/', views.plan_list, name='plan list'),
    path('posts/<int:pk>/', views.plan_detail),
    # path('posts/<id>', views.plan_list, name='plan list'),
    # url(r'^posts/(?P<pk>\d+)/$',views.plan_detail),
    
]
