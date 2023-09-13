# Generated by Django 4.2.4 on 2023-09-11 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id_business', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('desc', models.CharField(max_length=100)),
                ('opening_time', models.TimeField(default='07:00:00')),
                ('closing_time', models.TimeField(default='18:00:00')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id_request', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=1000)),
                ('price', models.IntegerField()),
                ('status', models.CharField(default='Sin tomar', max_length=30)),
                ('delivery_location', models.CharField(max_length=250)),
                ('desc_delivery', models.CharField(max_length=1000, null=True)),
                ('pick_up_location', models.CharField(default='Pick-up location', max_length=250)),
                ('desc_pick_up_location', models.CharField(max_length=1000, null=True)),
                ('fk_id_business', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bring_u.business')),
                ('fk_id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id_product', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('fk_id_business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bring_u.business')),
            ],
        ),
    ]
