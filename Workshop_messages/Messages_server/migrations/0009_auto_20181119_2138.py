# Generated by Django 2.1.2 on 2018-11-19 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Messages_server', '0008_auto_20181119_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groups',
            name='person',
        ),
        migrations.AddField(
            model_name='person',
            name='groups',
            field=models.ManyToManyField(to='Messages_server.Groups'),
        ),
    ]