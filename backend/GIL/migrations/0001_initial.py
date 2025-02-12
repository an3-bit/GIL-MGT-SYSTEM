# Generated by Django 5.1.3 on 2025-02-10 07:56

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('join_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('service', models.CharField(choices=[('land_survey', 'Land Survey'), ('title_search', 'Title Search'), ('land_transfer', 'Land Transfer'), ('subdivision', 'Subdivision')], default='land_survey', max_length=50)),
                ('process', models.CharField(choices=[('initial_submission', 'Initial Submission'), ('registry_processing', 'Registry Processing'), ('approval_verification', 'Approval & Verification'), ('ready_for_collection', 'Title Ready for Collection')], default='initial_submission', max_length=50)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'db_table': 'clients',
                'ordering': ['username'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('amount', models.IntegerField()),
                ('transaction_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(default='waiting for approval', max_length=200)),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
                'db_table': 'payments',
                'ordering': ['client_name'],
            },
        ),
        migrations.CreateModel(
            name='Surveyor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('status', models.CharField(default='inactive', max_length=200)),
                ('join_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_registered', models.BooleanField(default=False)),
                ('is_serving', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Surveyor',
                'verbose_name_plural': 'Surveyors',
                'db_table': 'surveyors',
                'ordering': ['username'],
            },
        ),
        migrations.CreateModel(
            name='TitleTransferTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Title Transfer Type',
                'verbose_name_plural': 'Title Transfer Types',
            },
        ),
        migrations.CreateModel(
            name='TitleDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('registry_processing', 'Registry Processing'), ('approval_verification', 'Approval and Verification'), ('ready_for_collection', 'Title Deed Ready for Collection')], default='registry_processing', max_length=50)),
                ('pdf_file', models.FileField(upload_to='title_documents/')),
                ('uploaded_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='GIL.client')),
            ],
            options={
                'verbose_name': 'Title Document',
                'verbose_name_plural': 'Title Documents',
                'ordering': ['-uploaded_at'],
            },
        ),
        migrations.CreateModel(
            name='TitleProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process', models.CharField(max_length=100)),
                ('message', models.TextField(default='Your process is now in this stage. Thank you!')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='processes', to='GIL.titletransfertypes')),
            ],
            options={
                'verbose_name': 'Title Process',
                'verbose_name_plural': 'Title Processes',
                'ordering': ['id'],
            },
        ),
    ]
