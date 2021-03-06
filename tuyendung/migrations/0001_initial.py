# Generated by Django 2.2.7 on 2020-03-17 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trangchu', '0002_auto_20200305_1945'),
    ]

    operations = [
        migrations.CreateModel(
            name='TuyenDung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tieu_de', models.CharField(max_length=255)),
                ('ngay_tao', models.DateTimeField()),
                ('mo_ta_ngan', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('noi_dung', models.TextField()),
                ('menu', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='trangchu.Menu')),
            ],
        ),
    ]
