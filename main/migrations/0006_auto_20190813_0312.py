# Generated by Django 2.2.3 on 2019-08-13 01:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190809_1712'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorial',
            old_name='tuttorial_pic',
            new_name='tutorial_pic',
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 13, 3, 12, 22, 340569), verbose_name='Date published'),
        ),
    ]