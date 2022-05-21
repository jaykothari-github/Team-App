from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('header/',views.header,name='header'),
    path('stock_view/',views.stock_view,name='stock_view'),
    path('stock_search/',views.stock_search,name='stock_search'),
]
