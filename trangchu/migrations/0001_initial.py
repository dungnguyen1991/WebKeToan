# Generated by Django 2.2.7 on 2020-02-28 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_title', models.CharField(max_length=255)),
                ('menu_link', models.CharField(max_length=500)),
                ('menu_parent', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='trangchu.Menu')),
            ],
        ),
    ]
