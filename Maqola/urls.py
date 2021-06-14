from django.urls import path
from .views import AlerListViewPost ,AlerDetailViewsPot,AlerCreateViews,AlerDeleteViews,AlerUpdateViews

urlpatterns = [
    path('',AlerListViewPost.as_view(),name='article'),
    path('<int:pk>/',AlerDetailViewsPot.as_view(),name='detail'),
    path('new/',AlerCreateViews.as_view(),name='create'),
    path('delete/<int:pk>/',AlerDeleteViews.as_view(),name='delete'),
    path('update/<int:pk>/',AlerUpdateViews.as_view(),name='update'),
    
   
]
