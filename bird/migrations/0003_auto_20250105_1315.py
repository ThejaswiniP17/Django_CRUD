# Generated by Django 3.2.25 on 2025-01-05 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bird', '0002_auto_20250105_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bird',
            name='bHabitat',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bird',
            name='bMigrationPattern',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='bird',
            name='bScientificName',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
