# Generated by Django 2.2.5 on 2019-09-28 14:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_auto_20190928_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=255)),
                ('is_ProcueStaff', models.BooleanField(default=False)),
                ('is_HRStaff', models.BooleanField(default=False)),
                ('is_DeliveryStaff', models.BooleanField(default=False)),
                ('is_Accountant', models.BooleanField(default=False)),
                ('is_SiteManager', models.BooleanField(default=False)),
                ('is_Inspector', models.BooleanField(default=False)),
            ],
        ),
    ]
