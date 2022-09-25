from django.urls import path
from django.views.generic import TemplateView
from .views import VesselView, AboutView


urlpatterns = [
    path('', VesselView.as_view(), name="home"),
    path('about/<str:pk>/', AboutView.as_view(), name='about'),
]