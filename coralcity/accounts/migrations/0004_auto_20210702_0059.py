# Generated by Django 3.2.4 on 2021-07-01 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_property_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='bathrooms',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='property',
            name='lot_size',
            field=models.IntegerField(default=0),
        ),
    ]
