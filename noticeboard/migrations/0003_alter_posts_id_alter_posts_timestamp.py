# Generated by Django 5.1.6 on 2025-02-11 10:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticeboard', '0002_alter_posts_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 11, 16, 10, 6, 842571)),
        ),
    ]
