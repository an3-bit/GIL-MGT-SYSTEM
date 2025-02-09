
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework import serializers

MOBILE_SASA_API_URL = "https://api.mobilesasa.com/v1/send-message"
MOBILE_SASA_API_KEY = "api_key_here"

class TitleTransferTypes(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Title Transfer Type"
        verbose_name_plural = "Title Transfer Types"

    def __str__(self):
        return self.name

class TitleProcess(models.Model):
    type = models.ForeignKey(
        TitleTransferTypes,
        on_delete=models.SET_NULL,
        null=True,
        related_name="processes",
    )
    process = models.CharField(max_length=100)
    message = models.TextField(default="Your process is now in this stage. Thank you!")

    class Meta:
        ordering = ['id']
        verbose_name = "Title Process"
        verbose_name_plural = "Title Processes"

    def __str__(self):
        return f"{self.type.name if self.type else 'No Type'} - {self.process}"

class Client(models.Model):
    SERVICE_CHOICES = [
        ("land_survey", "Land Survey"),
        ("title_search", "Title Search"),
        ("land_transfer", "Land Transfer"),
        ("subdivision", "Subdivision"),
    ]

    PROCESS_CHOICES = [
        ("initial_submission", "Initial Submission"),
        ("registry_processing", "Registry Processing"),
        ("approval_verification", "Approval & Verification"),
        ("ready_for_collection", "Title Ready for Collection"),
    ]

    username = models.CharField(max_length=100, unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    join_date = models.DateTimeField(default=timezone.now)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default='land_survey')
    process = models.CharField(max_length=50, choices=PROCESS_CHOICES, default='initial_submission')

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ['username']
        db_table = 'clients'

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Surveyor(models.Model):
    username = models.CharField(max_length=100, unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    status = models.CharField(max_length=200, default="inactive")
    join_date = models.DateTimeField(default=timezone.now)
    is_registered = models.BooleanField(default=False)
    is_serving = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Surveyor'
        verbose_name_plural = 'Surveyors'
        ordering = ['username']
        db_table = 'surveyors'

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Payment(models.Model):
    client_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    amount = models.IntegerField()
    transaction_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=200, default="waiting for approval")

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        ordering = ['client_name']
        db_table = 'payments'

    def __str__(self):
        return self.client_name

class TitleDocument(models.Model):
    STATUS_CHOICES = [
        ("registry_processing", "Registry Processing"),
        ("approval_verification", "Approval and Verification"),
        ("ready_for_collection", "Title Deed Ready for Collection"),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="documents")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="registry_processing")
    pdf_file = models.FileField(upload_to="title_documents/")
    uploaded_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Title Document"
        verbose_name_plural = "Title Documents"
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"{self.client.firstname} {self.client.lastname} - {self.status}"
