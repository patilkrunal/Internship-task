# Generated by Django 3.2.7 on 2021-09-07 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20210907_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='event_time',
        ),
        migrations.AlterField(
            model_name='events',
            name='event_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]