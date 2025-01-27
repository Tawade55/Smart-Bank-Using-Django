# Generated by Django 5.0.6 on 2024-07-18 09:33

import shortuuid.django_fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_transaction_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='number',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=22, max_length=20, prefix='451', unique=True),
        ),
    ]
