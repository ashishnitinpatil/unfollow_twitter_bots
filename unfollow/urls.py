from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('callback/', views.callback, name='auth_return'),
    path('logout/', views.unauth, name='oauth_unauth'),
    path('auth/', views.auth, name='oauth_auth'),
    path('info/', views.info, name='info'),
]
