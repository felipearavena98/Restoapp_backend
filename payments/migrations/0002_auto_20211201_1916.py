# Generated by Django 3.2.9 on 2021-12-01 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='paymentType',
            field=models.CharField(choices=[('CARD', 'card'), ('CASH', 'cash')], max_length=255),
        ),
        migrations.AlterField(
            model_name='payment',
            name='totalPayment',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
