from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateListView.as_view() , name='getAllRs'),
]