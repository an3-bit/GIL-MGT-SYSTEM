
from django.urls import path
from rest_framework.routers import DefaultRouter
from GIL.views import (
    TitleTransferTypesViewSet, TitleProcessViewSet,
    ClientViewSet, SurveyorViewSet,
    PaymentViewSet, TitleDocumentViewSet
)

# Initialize the router
router = DefaultRouter()

# Register ViewSets
router.register(r'title-transfer-types', TitleTransferTypesViewSet)
router.register(r'title-processes', TitleProcessViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'surveyors', SurveyorViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'title-documents', TitleDocumentViewSet)

urlpatterns = [
    # Client endpoints
    path('v1/clients/', ClientViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('v1/clients/<int:pk>/', ClientViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    
    # Surveyor endpoints
    path('v1/surveyors/', SurveyorViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('v1/surveyors/<int:pk>/', SurveyorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    
    # Payment endpoints
    path('v1/payments/', PaymentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('v1/payments/<int:pk>/', PaymentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    
    # Title Document endpoints
    path('v1/documents/', TitleDocumentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('v1/documents/<int:pk>/', TitleDocumentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    
    # Include the router URLs as well
    *router.urls,
]
