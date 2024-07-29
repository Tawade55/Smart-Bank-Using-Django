# Generated by Django 5.0.6 on 2024-07-18 09:42

import shortuuid.django_fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_creditcard_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='number',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=22, max_length=5, prefix='451', unique=True),
        ),
    ]
