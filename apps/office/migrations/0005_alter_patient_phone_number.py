# Generated by Django 4.1.5 on 2023-01-26 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0004_alter_patient_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(blank=True, max_length=16, null=True, unique=True, verbose_name='Номер телефона'),
        ),
    ]
