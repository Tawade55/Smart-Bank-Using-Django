# Generated by Django 5.0.6 on 2024-07-05 11:53

import django.db.models.deletion
import shortuuid.django_fields
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('account_balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('account_number', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=10, max_length=25, prefix='217')),
                ('account_id', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=7, max_length=25, prefix='DEX')),
                ('pin_number', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=4, max_length=25, prefix='')),
                ('ref_code', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefg1234567890', length=10, max_length=15, prefix='')),
                ('account_status', models.CharField(choices=[('active', 'Active'), ('in_active', 'In-active')], default='in_active', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('kyc_submitted', models.BooleanField(default=False)),
                ('kyc_confirmed', models.BooleanField(default=False)),
                ('recommended_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='recommended_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
