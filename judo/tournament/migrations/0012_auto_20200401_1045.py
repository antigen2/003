# Generated by Django 3.0.4 on 2020-04-01 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0011_auto_20200401_1029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gym',
            options={'ordering': ('short_name',), 'verbose_name': 'Тренер'},
        ),
    ]
