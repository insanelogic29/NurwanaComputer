# Generated by Django 2.0.4 on 2018-04-27 12:52

from django.db import migrations, models
import django.db.models.deletion
import produk.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id_kategori', models.AutoField(primary_key=True, serialize=False)),
                ('nama_kategori', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id_produk', models.AutoField(primary_key=True, serialize=False)),
                ('nama_produk', models.CharField(max_length=250)),
                ('stok_produk', models.IntegerField()),
                ('harga_produk', models.IntegerField()),
                ('rating_produk', models.IntegerField()),
                ('foto_produk', models.FileField(blank=True, null=True, upload_to=produk.models.Produk.content_file_name)),
                ('kategori_produk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kategori', to='produk.Kategori')),
            ],
        ),
    ]