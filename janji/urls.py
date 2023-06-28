from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateListView.as_view() , name='getAllJanji'),
    path('myjanji/', views.GetMyJanjiView.as_view() , name='getMyJanji')
]