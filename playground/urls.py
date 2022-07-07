from django.urls import path, include
from rest_framework_nested import routers

from playground import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)

review_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
review_router.register('review', views.ReviewViewSet, basename='product-review')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(review_router.urls)),

]
