# Generated by Django 2.2.3 on 2019-08-05 19:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190727_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 5, 21, 41, 9, 221683), verbose_name='Date published'),
        ),
    ]