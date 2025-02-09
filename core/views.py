
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import (
    TitleTransferTypes, TitleProcess, Client, 
    Surveyor, Payment, TitleDocument
)
from .serializers import (
    TitleTransferTypesSerializer, TitleProcessSerializer,
    ClientSerializer, SurveyorSerializer,
    PaymentSerializer, TitleDocumentSerializer
)

class TitleTransferTypesViewSet(viewsets.ModelViewSet):
    queryset = TitleTransferTypes.objects.all()
    serializer_class = TitleTransferTypesSerializer
    permission_classes = [permissions.IsAuthenticated]

class TitleProcessViewSet(viewsets.ModelViewSet):
    queryset = TitleProcess.objects.all()
    serializer_class = TitleProcessSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def documents(self, request, pk=None):
        client = self.get_object()
        documents = TitleDocument.objects.filter(client=client)
        serializer = TitleDocumentSerializer(documents, many=True)
        return Response(serializer.data)

class SurveyorViewSet(viewsets.ModelViewSet):
    queryset = Surveyor.objects.all()
    serializer_class = SurveyorSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def toggle_status(self, request, pk=None):
        surveyor = self.get_object()
        surveyor.is_serving = not surveyor.is_serving
        surveyor.status = "active" if surveyor.is_serving else "inactive"
        surveyor.save()
        return Response({'status': surveyor.status})

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

class TitleDocumentViewSet(viewsets.ModelViewSet):
    queryset = TitleDocument.objects.all()
    serializer_class = TitleDocumentSerializer
    permission_classes = [permissions.IsAuthenticated]
