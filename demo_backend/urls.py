from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .api import userDataApi

urlpatterns = [
    path('api/userData',userDataApi.as_view()),
    path('api/userData/<str:pk>',userDataApi.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]