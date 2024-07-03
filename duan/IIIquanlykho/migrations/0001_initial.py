# Generated by Django 5.0.4 on 2024-05-09 14:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Ithongtincongty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NhomHang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_nhom_hang', models.CharField(max_length=100, unique=True, verbose_name='Tên nhóm hàng')),
                ('hoat_dong', models.BooleanField(default=True, verbose_name='Hoạt động')),
            ],
            options={
                'verbose_name': 'Nhóm hàng',
                'verbose_name_plural': '5. Nhóm hàng',
            },
        ),
        migrations.CreateModel(
            name='NhomVang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_nhom_vang', models.CharField(max_length=100, unique=True, verbose_name='Tên nhóm vàng')),
                ('hoat_dong', models.BooleanField(default=True, verbose_name='Hoạt động')),
            ],
            options={
                'verbose_name': 'Nhóm vàng',
                'verbose_name_plural': '3. Nhóm vàng',
            },
        ),
        migrations.CreateModel(
            name='LoaiVang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_loai_vang', models.CharField(max_length=100, unique=True, verbose_name='Tên loại vàng')),
                ('tuoi_vang', models.FloatField(default=0, verbose_name='Tuổi vàng')),
                ('tuoi_pho', models.CharField(default=0, max_length=50, verbose_name='Tuổi phổ')),
                ('tien_te', models.CharField(choices=[('1', 'VND'), ('2', 'SIN'), ('3', 'THAI'), ('4', 'UC'), ('5', 'USD'), ('6', 'USD (1-2)'), ('7', 'USD (5-10-2)')], default=1, max_length=100, verbose_name='Tiền tệ')),
                ('doi', models.IntegerField(default=0, verbose_name='Đổi')),
                ('don_vi_tinh', models.CharField(choices=[('1', 'Ly'), ('2', 'Gram'), ('3', 'Món')], max_length=100, verbose_name='Đơn vị tính')),
                ('do_uu_tien', models.IntegerField(blank=True, null=True, verbose_name='Độ ưu tiên')),
                ('don_gia_bu', models.IntegerField(default=0, verbose_name='Đơn giá bù/Tiền bù')),
                ('phantram_giabu', models.IntegerField(default=0, verbose_name='% Giá trị bù')),
                ('hien_bang_dientu', models.CharField(default=0, max_length=255, verbose_name='Tên hiển thị bảng điện tử')),
                ('ghi_chu', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ghi chú')),
                ('khoang_cach_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Khoảng cách 1')),
                ('khoang_cach_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Khoảng cách 2')),
                ('khoang_cach_3', models.CharField(blank=True, max_length=255, null=True, verbose_name='Khoảng cách 3')),
                ('khoang_cach_4', models.CharField(blank=True, max_length=255, null=True, verbose_name='Khoảng cách 4')),
                ('tygia_min', models.IntegerField(default=0, verbose_name='% Tỷ giá min')),
                ('tygia_max', models.IntegerField(default=0, verbose_name='% Tỷ giá max')),
                ('giamgia_bansi', models.IntegerField(blank=True, null=True, verbose_name='Giảm giá bán sỉ')),
                ('don_vi_can', models.CharField(choices=[('1', 'Lượng'), ('2', 'Chỉ'), ('3', 'Phân'), ('3', 'Ly')], max_length=50, verbose_name='Đơn vị cân')),
                ('lamtron_giamuaban', models.CharField(choices=[('1', 'Đơn vị ngàn đồng'), ('2', 'Đơn vị chục ngàn đồng'), ('3', 'Đơn vị trăm ngàn đồng'), ('4', 'Đơn vị triệu đồng'), ('5', 'Không làm tròn')], max_length=150, verbose_name='Làm tròn giá mua bán')),
                ('hienbang_dientu', models.BooleanField(blank=True, null=True, verbose_name='Hiện bảng điện tử')),
                ('hoat_dong', models.BooleanField(default=True, verbose_name='Hoạt động')),
                ('nhom_vang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='IIIquanlykho.nhomvang', verbose_name='Thuộc nhóm vàng')),
            ],
            options={
                'verbose_name': 'Loại vàng',
                'verbose_name_plural': '4. Loại vàng',
            },
        ),
        migrations.CreateModel(
            name='QuayLon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_quay_lon', models.CharField(max_length=255, unique=True, verbose_name='Tên quầy lớn')),
                ('hoat_dong', models.BooleanField(default=True, verbose_name='Hoạt động')),
                ('chi_nhanh', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quay_lons', to='Ithongtincongty.chinhanh', verbose_name='Thuộc chi nhánh')),
            ],
            options={
                'verbose_name': 'Quầy lớn',
                'verbose_name_plural': '1. Quầy lớn',
            },
        ),
        migrations.CreateModel(
            name='QuayNho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_quay_nho', models.CharField(max_length=255, unique=True, verbose_name='Tên quầy nhỏ')),
                ('trong_luong_khay_ly', models.IntegerField(default=0, verbose_name='Trọng lượng khay ly')),
                ('trong_luong_khay_gram', models.IntegerField(default=0, verbose_name='Trọng lượng khay gram')),
                ('hoat_dong', models.BooleanField(default=True, verbose_name='Hoạt động')),
                ('chi_nhanh', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quay_nhos', to='Ithongtincongty.chinhanh', verbose_name='Thuộc chi nhánh')),
                ('quay_lon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quay_nhos', to='IIIquanlykho.quaylon', verbose_name='Thuộc quầy lớn')),
            ],
            options={
                'verbose_name': 'Quầy nhỏ',
                'verbose_name_plural': '2. Quầy nhỏ',
            },
        ),
        migrations.CreateModel(
            name='NhapHang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_nhan_vien', models.CharField(choices=[('1', 'Chưa code'), ('2', 'Code sau')], max_length=100, verbose_name='Nhân viên nhập hàng')),
                ('ten_chi_nhanh', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nhap_hangs', to='Ithongtincongty.chinhanh', verbose_name='Chi nhánh')),
                ('quay_lon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='IIIquanlykho.quaylon', verbose_name='Thuộc quầy lớn')),
                ('quay_nho', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nhap_hangs', to='IIIquanlykho.quaynho', verbose_name='Quầy nhỏ')),
            ],
            options={
                'verbose_name': 'Nhập hàng',
                'verbose_name_plural': '6. Nhập hàng',
            },
        ),
        migrations.CreateModel(
            name='SanPham',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_san_pham', models.CharField(max_length=255, verbose_name='Tên sản phẩm')),
                ('ma_vach', models.ImageField(blank=True, upload_to='ma_vach', verbose_name='Mã vạch')),
                ('hinh_anh', models.ImageField(blank=True, null=True, upload_to='san_pham', verbose_name='Hình ảnh')),
                ('tinh_trang', models.CharField(default='Còn hàng', max_length=255, verbose_name='Tình trạng')),
                ('hoat_dong', models.BooleanField(default=True, verbose_name='Hoạt động')),
                ('loai_vang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='san_phams', to='IIIquanlykho.loaivang', verbose_name='Loại vàng')),
                ('nhom_hang', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='san_phams', to='IIIquanlykho.nhomhang', verbose_name='Thuộc nhóm hàng')),
                ('ten_chi_nhanh', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='san_phams', to='Ithongtincongty.chinhanh', verbose_name='Chi nhánh')),
            ],
            options={
                'verbose_name': 'Sản phẩm',
                'verbose_name_plural': '7. Sản phẩm',
            },
        ),
    ]