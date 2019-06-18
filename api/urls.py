from django.urls import path, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('request_yaml/', views.YamlDetail.as_view())
]
