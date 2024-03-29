# Generated by Django 2.2.5 on 2019-09-30 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0001_initial'),
        ('order', '0012_auto_20191001_0457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='approval',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='order_id',
        ),
        migrations.AddField(
            model_name='invoice',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.Order'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='supplier.Supplier'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='amount_due',
            field=models.FloatField(blank=True),
        ),
    ]
