# Generated by Django 3.0.8 on 2020-07-08 10:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_auto_20200702_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
