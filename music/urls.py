from django.urls import path
from . import views

app_name='music'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
     path('register/',views.UserFormView.as_view(),name='register'),

    path('<int:pk>/',views.DetailsView.as_view(),name='details'),
    
    path('album/add/',views.AlbumCreate.as_view(),name='album-add'),
    path('<int:pk>/',views.AlbumUpdate.as_view(),name='album-update'),
    path('<int:pk>/delete/',views.AlbumDelete.as_view(),name='album-delete'),
]

