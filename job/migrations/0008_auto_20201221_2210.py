# Generated by Django 3.1.3 on 2020-12-21 20:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0007_auto_20201220_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='likers',
            field=models.ManyToManyField(related_name='liked_jobs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='job',
            name='likes_num',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]