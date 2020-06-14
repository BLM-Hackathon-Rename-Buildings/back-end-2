# Generated by Django 3.0.7 on 2020-06-14 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('symbols', '0003_auto_20200614_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symbol',
            name='honoree',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='symbols.Honoree'),
        ),
        migrations.AlterField(
            model_name='symbol',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to=''),
            preserve_default=False,
        ),
    ]
