from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='logi'),
    path('logout/', views.logout_user, name='logout'),
    path('cabinet/', views.cabinet, name='cabinet'),
    path('take_key/<int:key_id>/', views.take_key, name='take_key'),  
    path('return_key/<int:key_id>/', views.return_key, name='return_key')  
]
