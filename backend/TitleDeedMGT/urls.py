
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from GIL .views import (
    TitleTransferTypesViewSet, TitleProcessViewSet,
    ClientViewSet, SurveyorViewSet,
    PaymentViewSet, TitleDocumentViewSet,UserRegistrationView, UserLoginView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()

router.register(r'title-transfer-types', TitleTransferTypesViewSet)
router.register(r'title-processes', TitleProcessViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'surveyors', SurveyorViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'title-documents', TitleDocumentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    # Authentication endpoints
    path('api/v1/register/', UserRegistrationView.as_view(), name='register'),
    path('api/v1/login/', UserLoginView.as_view(), name='login'),
    path('api/v1/', include(router.urls)),

    #Client endpoints
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
    path('v1/documents/<int:pk>/',
         TitleDocumentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # Include the router URLs as well
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    *router.urls,
]