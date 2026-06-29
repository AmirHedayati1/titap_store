from django.urls import path
from products import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categories', views.CategoriesView)
router.register('products', views.ProductsViewset)


urlpatterns = router.urls