# Generated by Django 4.2.4 on 2023-09-12 03:33

import bring_u.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bring_u', '0002_request_fk_id_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='file',
            field=models.FileField(null=True, upload_to=bring_u.models.upload_to),
        ),
    ]
