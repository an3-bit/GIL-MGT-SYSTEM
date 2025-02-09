
from rest_framework import serializers
from .models import (
    TitleTransferTypes, TitleProcess, Client, 
    Surveyor, Payment, TitleDocument
)

class TitleTransferTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitleTransferTypes
        fields = '__all__'

class TitleProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitleProcess
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class SurveyorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surveyor
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class TitleDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitleDocument
        fields = '__all__'
