from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from store import views

router = routers.DefaultRouter()
# router = DefaultRouter()
router.register('products', views.ProductViewSet, basename='product')

review_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
review_router.register('reviews', views.ReviewViewSet, basename='product-review')

router.register('customers', views.CustomerViewSet, basename='customer')

router.register('carts', views.CartViewSet, basename='cart')

cartitem_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cartitem_router.register('cartitems', views.CartItemViewSet, basename="cart-cartitem")

urlpatterns = [
    path('', include(router.urls)),
    path('', include(review_router.urls)),
    path('', include(cartitem_router.urls)),
    path('test/', views.test),
]
