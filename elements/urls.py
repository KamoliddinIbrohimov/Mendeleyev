from django.urls import path, include

from rest_framework.routers import DefaultRouter
from elements import views

router = DefaultRouter()
router.register('elements', views.ElementsViewSet)

urlpatterns = [
    path('', include(router.urls))
]