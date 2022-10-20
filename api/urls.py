from django.urls import path
import api.views as views

urlpatterns = [
    path('product-create/', views.ProductCreateView.as_view()),
]