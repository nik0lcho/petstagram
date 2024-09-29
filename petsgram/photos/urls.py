from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views.add, name='add'),
    path('<int:pk>/', include([
        path('', views.photo_details, name='photo_details'),
        path('edit/', views.photo_edit, name='photo_edit'),
    ]))
]
