
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TitleTransferTypesViewSet, TitleProcessViewSet,
    ClientViewSet, SurveyorViewSet,
    PaymentViewSet, TitleDocumentViewSet
)

router = DefaultRouter()
router.register(r'title-transfer-types', TitleTransferTypesViewSet)
router.register(r'title-processes', TitleProcessViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'surveyors', SurveyorViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'title-documents', TitleDocumentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
