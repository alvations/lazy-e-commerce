# Generated by Django 2.1.2 on 2018-12-01 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokopedia', '0024_auto_20181201_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='barang_harga_jual',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='good',
            name='barang_rating',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Jumlah Bintang'),
        ),
        migrations.AlterField(
            model_name='good',
            name='barang_rating_count',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Jumlah Pemberi Bintang'),
        ),
    ]
