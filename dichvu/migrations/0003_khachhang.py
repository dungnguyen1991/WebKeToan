# Generated by Django 2.2.7 on 2020-03-17 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trangchu', '0002_auto_20200305_1945'),
        ('dichvu', '0002_phidichvu'),
    ]

    operations = [
        migrations.CreateModel(
            name='KhachHang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tieu_de', models.CharField(max_length=255)),
                ('noi_dung', models.TextField()),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trangchu.Menu')),
            ],
        ),
    ]
