from django.urls import path
from . import views


urlpatterns = [
    path('deposit-products/', views.deposit_products, name = 'deposit-products'),
    path('deposit-products/<str:fin_prdt_cd>/', views.deposit_products_detail, name = 'deposit-products-options'),
    path('saving-products/', views.saving_products, name = 'saving-products'),
    path('saving-products/<str:fin_prdt_cd>/', views.saving_products_detail, name = 'saving-products-options'),
    path('recommend-products/', views.recommend_products, name = 'recommend'),
]
