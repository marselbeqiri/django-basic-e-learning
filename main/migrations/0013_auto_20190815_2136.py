# Generated by Django 2.2.3 on 2019-08-15 19:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20190815_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 15, 21, 36, 9, 342450), verbose_name='Date published'),
        ),
    ]