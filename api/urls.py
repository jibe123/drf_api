from django.urls import path
import api.views as views

urlpatterns = [
    path('product-create/', views.ProductAPIView.as_view()),
    path('product/<int:pk>/', views.ProductAPIView.as_view()),
]