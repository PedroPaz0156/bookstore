from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from product.views import CategoryViewSet, ProductViewSet
from order.views import OrderViewSet

router = DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("products", ProductViewSet)
router.register("orders", OrderViewSet)

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    re_path('bookstore/(?P<version>(v1|v2))/', include('order.urls')),
    re_path('bookstore/(?P<version>(v1|v2))/', include('product.urls')),
]
