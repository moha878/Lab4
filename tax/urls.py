from django.urls import path
from . import views

urlpatterns = [
    # Default path to index view
    path("", views.index, name="index"),
    # Path to calculate view with a number parameter
    path('<int:num>/', views.calculate, name='calculate'),
    # Path to tax rate view
    path('taxrate/', views.tax_rate, name='tax_rate'),
]