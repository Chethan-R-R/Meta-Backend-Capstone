from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('',views.index),
    path('menu-items/',views.MenuItemView.as_view(),name='menu-list'),
    path('menu-item/<int:pk>',views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]