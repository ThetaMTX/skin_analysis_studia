from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('upload/', views.upload_image, name='upload_image'),
    path('edit/<int:image_id>/', views.edit_image, name='edit_image'),
    path('delete/<int:image_id>/', views.delete_image, name='delete_image'),
    path('', views.image_list, name='image_list'),
]
