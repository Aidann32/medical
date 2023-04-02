# Generated by Django 4.1.7 on 2023-04-01 00:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('office', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='xrayrequest',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='xrayrequest',
            name='x_ray',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office.xray'),
        ),
        migrations.AddField(
            model_name='xray',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office.patient'),
        ),
        migrations.AddField(
            model_name='patient',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office.patient', verbose_name='Пациент'),
        ),
    ]