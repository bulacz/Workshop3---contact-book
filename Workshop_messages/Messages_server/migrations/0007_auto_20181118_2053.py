# Generated by Django 2.1.2 on 2018-11-18 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Messages_server', '0006_auto_20181118_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='group',
            field=models.ManyToManyField(to='Messages_server.Groups'),
        ),
    ]