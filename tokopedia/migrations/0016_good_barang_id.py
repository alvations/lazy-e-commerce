# Generated by Django 2.1.2 on 2018-11-30 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokopedia', '0015_auto_20181130_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='barang_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
