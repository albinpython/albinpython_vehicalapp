from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('curd/',views.curd,name='curd'),
    path('',views.curdview,name='curdview'),
    path('delete/<int:crudid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),


]
