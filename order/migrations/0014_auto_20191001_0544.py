# Generated by Django 2.2.5 on 2019-10-01 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_auto_20191001_0518'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='supplier',
            new_name='supplier_product',
        ),
    ]
