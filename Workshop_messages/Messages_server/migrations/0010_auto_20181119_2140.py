# Generated by Django 2.1.2 on 2018-11-19 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Messages_server', '0009_auto_20181119_2138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='groups',
            new_name='group',
        ),
    ]
