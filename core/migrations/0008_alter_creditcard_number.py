# Generated by Django 5.0.6 on 2024-07-18 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_creditcard_card_id_alter_creditcard_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='number',
            field=models.IntegerField(),
        ),
    ]