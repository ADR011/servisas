from django.urls import path

from . import views

urlpatterns = [
    path('', views.sarasas),
    path('<int:pk>', views.issamiau),
]
