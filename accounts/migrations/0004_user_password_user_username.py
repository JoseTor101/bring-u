# Generated by Django 4.2.4 on 2023-09-03 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='123', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=123, max_length=15),
            preserve_default=False,
        ),
    ]
