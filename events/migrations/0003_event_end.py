# Generated by Django 2.1.2 on 2018-11-03 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]