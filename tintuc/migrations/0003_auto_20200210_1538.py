# Generated by Django 2.2.7 on 2020-02-10 08:38

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('tintuc', '0002_auto_20200210_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tintuc',
            name='mo_ta_ngan',
            field=tinymce.models.HTMLField(),
        ),
    ]
