# Generated by Django 2.2.7 on 2020-03-23 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hoten', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('tencongty', models.CharField(max_length=255)),
                ('diachi', models.CharField(max_length=255)),
                ('dienthoai', models.CharField(max_length=10)),
                ('fax', models.CharField(max_length=10)),
                ('guiden', models.EmailField(max_length=255)),
                ('tieude', models.CharField(max_length=255)),
                ('noidung', models.TextField()),
            ],
        ),
    ]
