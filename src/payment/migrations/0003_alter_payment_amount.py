# Generated by Django 5.1.4 on 2025-01-02 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_rename_withdrawalrequest_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.FloatField(max_length=100),
        ),
    ]
