# Generated by Django 3.0.4 on 2020-05-07 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0018_auto_20200507_1130'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='competitor',
            unique_together={('tournament', 'judoka')},
        ),
    ]