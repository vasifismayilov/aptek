from django.urls import path
from . import views

urlpatterns = [
    path('', views.drug_list, name='drug-list'),
    path('delete-drug/<int:pk>/', views.delete_drug, name='delete-drug'),
    path('drug-edit/<int:pk>/', views.update_drug, name='drug-edit'),
    path('factory-list/', views.factory_list, name='factory-list')
]
