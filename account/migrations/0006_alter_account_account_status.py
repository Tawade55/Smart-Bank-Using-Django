# Generated by Django 5.0.6 on 2024-07-14 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_kyc_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_status',
            field=models.CharField(choices=[('active', 'Active'), ('in_active', 'In-active'), ('pending', 'Pending')], default='in_active', max_length=100),
        ),
    ]
