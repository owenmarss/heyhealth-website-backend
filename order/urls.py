from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateListView.as_view(), name='getAllOrders'),
    path('myorder/', views.GetMyOrderView.as_view(), name='getMyOrders')
]