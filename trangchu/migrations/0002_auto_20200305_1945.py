# Generated by Django 2.2.7 on 2020-03-05 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trangchu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='menu_order',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='menu',
            name='menu_parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='trangchu.Menu'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='menu_title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
