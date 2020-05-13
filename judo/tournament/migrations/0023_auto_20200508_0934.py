# Generated by Django 3.0.4 on 2020-05-08 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0022_tournamenttable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournamenttable',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tournament_tables', to='tournament.Tournament', verbose_name='Турнир'),
        ),
        migrations.CreateModel(
            name='TournamentTableGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(choices=[('A', 'Группа А'), ('B', 'Группа Б')], default='A', max_length=1, verbose_name='Турнирная группа')),
                ('slug', models.SlugField(max_length=250, verbose_name='Алиас')),
                ('tournament_table', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='table_groups', to='tournament.TournamentTable', verbose_name='Турнирная таблица')),
            ],
        ),
    ]