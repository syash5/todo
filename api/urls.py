from .views import TodoRud
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todo',TodoRud)

urlpatterns = [
    path('',include(router.urls), name='todorud'),

]