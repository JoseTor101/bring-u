# Generated by Django 4.2.4 on 2023-09-12 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bring_u', '0004_remove_request_fk_id_business'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='business_name',
            field=models.CharField(max_length=70, null=True),
        ),
    ]
