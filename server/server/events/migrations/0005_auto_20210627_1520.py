# Generated by Django 3.1.11 on 2021-06-27 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20210624_1822'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-start_time']},
        ),
    ]
