# Generated by Django 2.1.2 on 2018-11-18 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Messages_server', '0003_auto_20181118_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='adress',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Messages_server.Adress'),
        ),
    ]