# Generated by Django 5.0.4 on 2024-05-15 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IIIquanlykho', '0002_remove_sanpham_hinh_anh_remove_sanpham_loai_vang_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='loaivang',
            name='so_thu_tu',
            field=models.CharField(blank='', default=0, editable=False, max_length=10, verbose_name='STT'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nhaphang',
            name='so_thu_tu',
            field=models.CharField(blank='', default=0, editable=False, max_length=10, verbose_name='STT'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nhomhang',
            name='so_thu_tu',
            field=models.CharField(blank='', default=0, editable=False, max_length=10, verbose_name='STT'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nhomvang',
            name='so_thu_tu',
            field=models.CharField(blank='', default=0, editable=False, max_length=10, verbose_name='STT'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quaylon',
            name='so_thu_tu',
            field=models.CharField(blank='', default=0, editable=False, max_length=10, verbose_name='STT'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quaynho',
            name='so_thu_tu',
            field=models.CharField(blank='', default=0, editable=False, max_length=10, verbose_name='STT'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sanpham',
            name='so_thu_tu',
            field=models.CharField(blank='', default=0, editable=False, max_length=10, verbose_name='STT'),
            preserve_default=False,
        ),
    ]
