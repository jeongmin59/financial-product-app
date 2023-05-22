# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views


urlpatterns = [
    path('', views.article_list),
    path('<int:article_pk>/', views.article_detail),
    path('<int:article_pk>/comments/', views.comment_create),
    path('<int:article_pk>/<int:comment_pk>/', views.comment_detail),
    path('<int:article_pk>/<int:comment_pk>/like/', views.comment_like),
]