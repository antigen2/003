# Generated by Django 3.0.4 on 2020-03-25 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0002_organization_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
    ]
