from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('documentation/', views.documentation, name='documentation'),
    path('contact/', views.contact, name='contact'),
    path('features/', views.features, name='features'),
    path('upload/', views.upload, name='upload'),
    path('api/', include('api.urls')),
]
