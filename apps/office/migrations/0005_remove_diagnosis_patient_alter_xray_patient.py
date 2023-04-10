# Generated by Django 4.1.7 on 2023-04-10 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0004_xrayrequest_doctor_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diagnosis',
            name='patient',
        ),
        migrations.AlterField(
            model_name='xray',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office.patient', verbose_name='Пациент'),
        ),
    ]
