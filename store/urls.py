from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from store import views

router = routers.DefaultRouter()
# router = DefaultRouter()

router.register('categories', views.CategoryViewSet, basename='category')

router.register('stores', views.StoreViewSet, basename='store')

router.register('products', views.ProductViewSet, basename='product')

review_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
review_router.register('reviews', views.ReviewViewSet, basename='product-review')

router.register('customers', views.CustomerViewSet, basename='customer')

router.register('carts', views.CartViewSet, basename='cart')

cartitem_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cartitem_router.register('cartitems', views.CartItemViewSet, basename="cart-cartitem")

router.register('orders', views.OrderViewSet, basename='order')

orderitem_router = routers.NestedDefaultRouter(router, 'orders', lookup='order')
orderitem_router.register('orderitems', views.OrderItemViewSet, basename="order-orderitem")

urlpatterns = [
    path('', include(router.urls)),
    path('', include(review_router.urls)),
    path('', include(cartitem_router.urls)),
    path('', include(orderitem_router.urls)),
    path('test/', views.test),
]
