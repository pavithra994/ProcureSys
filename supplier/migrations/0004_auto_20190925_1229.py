# Generated by Django 2.2.5 on 2019-09-25 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0003_auto_20190925_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplierproductinfo',
            name='Product_type',
            field=models.CharField(max_length=100),
        ),
    ]