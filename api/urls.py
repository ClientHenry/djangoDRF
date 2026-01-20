from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet) # 自动生成 /books/ 路由

urlpatterns = [
    path('', include(router.urls)),
]