from django.urls import path, include
from .views import add_item, summary

urlpatterns = [
    path('', add_item, name='add-item'),
    path('summary/', summary, name='summary')
]
