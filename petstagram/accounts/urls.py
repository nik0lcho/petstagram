from django.urls import path, include
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/<int:pk>/', include([
        path('', views.show_profile_details, name='show_profile_details'),
        path('edit/', views.edit_profile, name='edit_profile'),
        path('delete/', views.delete_profile, name='delete_profile'),
    ]))
]
