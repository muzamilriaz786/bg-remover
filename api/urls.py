from django.urls import path
from .views import RemoveBackgroundView

urlpatterns = [
    path('remove/', RemoveBackgroundView.as_view(), name='remove-background'),
]
