# Generated by Django 5.1.6 on 2025-02-11 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GIL', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
