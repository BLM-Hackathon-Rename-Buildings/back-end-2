# Generated by Django 3.0.7 on 2020-08-09 23:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('symbols', '0005_honoree_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='honoree',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 9, 23, 2, 54, 8445, tzinfo=utc)),
        ),
    ]