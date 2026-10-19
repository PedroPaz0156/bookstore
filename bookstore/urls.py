from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from product.views import CategoryViewSet, ProductViewSet
from order.views import OrderViewSet

router = DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("products", ProductViewSet)
router.register("orders", OrderViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
