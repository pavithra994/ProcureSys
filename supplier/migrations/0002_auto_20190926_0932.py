# Generated by Django 2.2.5 on 2019-09-26 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplierproductinfo',
            name='Amount',
            field=models.FloatField(),
        ),
    ]
