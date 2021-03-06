# Generated by Django 2.1.2 on 2018-11-01 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('start', models.DateTimeField()),
                ('city', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(blank=True, max_length=300)),
                ('place', models.CharField(blank=True, max_length=300)),
                ('comment', models.TextField(blank=True)),
            ],
        ),
    ]
