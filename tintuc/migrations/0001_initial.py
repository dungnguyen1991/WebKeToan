# Generated by Django 2.2.7 on 2020-02-07 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TinTuc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tieu_de', models.CharField(max_length=255)),
                ('ngay_tao', models.DateTimeField()),
                ('mo_ta_ngan', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('noi_dung', models.TextField()),
            ],
        ),
    ]
