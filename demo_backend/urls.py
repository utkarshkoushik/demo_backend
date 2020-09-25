from django.urls import path, include
from .api import userDataApi

urlpatterns = [
    path('api/userData',userDataApi.as_view()),
    path('api/userData/<str:pk>',userDataApi.as_view())
]