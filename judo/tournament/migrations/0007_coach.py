# Generated by Django 3.0.4 on 2020-04-01 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0006_auto_20200325_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=25, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=25, verbose_name='Имя')),
                ('middle_name', models.CharField(max_length=25, verbose_name='Отчество')),
                ('short_name', models.CharField(max_length=25, verbose_name='Фамилия и инициалы')),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='coaches', to='tournament.Gym', verbose_name='Спортивный зал')),
            ],
            options={
                'ordering': ('last_name', 'first_name', 'middle_name'),
            },
        ),
    ]