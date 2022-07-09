from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from store import views

# router = routers.DefaultRouter()
router = DefaultRouter()
router.register('products', views.ProductViewSet, basename='product')

review_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
review_router.register('review', views.ReviewViewSet, basename='product-review')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(review_router.urls)),
    path('test/', views.test),
]
