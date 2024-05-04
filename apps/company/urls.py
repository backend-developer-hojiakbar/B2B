from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'country', CountryViewSet, basename='country')
router.register(r'company', CompanyViewSet, basename='company')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'articles', ArticlesViewSet, basename='articles')
router.register(r'quote', QuoteViewSet, basename='quote')

urlpatterns = [
    path('router/', include(router.urls))
]