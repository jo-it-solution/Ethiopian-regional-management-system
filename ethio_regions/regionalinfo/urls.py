from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('create_region/', views.create_region, name='create_region'),
    path('detail_region/<int:pk>', views.detail_region, name='detail_region'),
    path('update_region/<int:pk>', views.update_region, name='update_region'),
    path('delete_region/<int:pk>', views.delete_region, name='delete_region'),
    path('user_register/>', views.user_register, name='user_register'),

]

