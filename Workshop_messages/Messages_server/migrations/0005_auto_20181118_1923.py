# Generated by Django 2.1.2 on 2018-11-18 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Messages_server', '0004_auto_20181118_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='adress',
            field=models.ForeignKey(null=True, on_delete=models.SET(None), to='Messages_server.Adress'),
        ),
    ]
