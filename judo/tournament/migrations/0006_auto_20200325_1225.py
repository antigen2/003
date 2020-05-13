# Generated by Django 3.0.4 on 2020-03-25 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0005_gym_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gym',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='gyms', to='tournament.Organization'),
            preserve_default=False,
        ),
    ]