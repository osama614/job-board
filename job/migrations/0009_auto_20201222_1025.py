# Generated by Django 3.1.3 on 2020-12-22 08:25

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_auto_20201221_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='cover_letter',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]