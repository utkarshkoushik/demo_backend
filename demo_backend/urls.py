from django.urls import path, include
# from django.conf.urls import url
from .api import userDataApi
# from rest_framework import routers

# router= routers.DefaultRouter()

urlpatterns = [
    path('api/userData',userDataApi.as_view()),
    path('api/userData/<str:pk>',userDataApi.as_view())
]