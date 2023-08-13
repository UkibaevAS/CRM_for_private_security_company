from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import WorkerViewSet, WorkerWithCategoryViewSet, WorkerWithoutCategoryViewSet


app_name = "worker"

router1 = DefaultRouter()
router1.register('worker_view', WorkerViewSet)

router2 = DefaultRouter()
router2.register('category', WorkerWithCategoryViewSet)

router3 = DefaultRouter()
router3.register('_category', WorkerWithoutCategoryViewSet)

urlpatterns = [
    path('', include(router1.urls)),
    path('with_', include(router2.urls)),
    path('without', include(router3.urls)),
]

