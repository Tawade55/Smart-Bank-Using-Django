# Generated by Django 5.0.6 on 2024-07-06 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_account_account_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kyc',
            name='identity_image',
            field=models.ImageField(blank=True, null=True, upload_to='kyc'),
        ),
    ]