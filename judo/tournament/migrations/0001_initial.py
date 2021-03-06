# Generated by Django 3.0.4 on 2020-03-24 12:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('short_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=100, unique_for_date=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('short_name',),
            },
        ),
    ]
