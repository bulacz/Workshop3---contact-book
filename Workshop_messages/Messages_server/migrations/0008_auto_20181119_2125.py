# Generated by Django 2.1.2 on 2018-11-19 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Messages_server', '0007_auto_20181118_2053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='group',
        ),
        migrations.AddField(
            model_name='groups',
            name='person',
            field=models.ManyToManyField(to='Messages_server.Person'),
        ),
    ]
