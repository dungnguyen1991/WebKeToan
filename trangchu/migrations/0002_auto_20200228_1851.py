# Generated by Django 2.2.7 on 2020-02-28 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trangchu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='menu_parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='trangchu.Menu'),
        ),
    ]
