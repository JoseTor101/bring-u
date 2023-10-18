# Generated by Django 4.2.4 on 2023-09-30 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bring_u', '0008_remove_delivery_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id_chat', models.AutoField(primary_key=True, serialize=False)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('fk_id_delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bring_u.delivery')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id_message', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('fk_id_chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.chat')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]