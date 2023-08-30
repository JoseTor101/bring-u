# Generated by Django 4.2.4 on 2023-08-30 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bring_u', '0002_business_product_request_user_delete_menu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='id_business',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='id_product',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='request',
            name='id_request',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id_user',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
