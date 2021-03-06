# Generated by Django 2.2.5 on 2019-10-07 11:26

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0006_auto_20190917_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='collecteddata',
            name='targeted',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=20, verbose_name='Targeted'),
        ),
        migrations.AddField(
            model_name='historicalcollecteddata',
            name='targeted',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=20, verbose_name='Targeted'),
        ),
    ]
