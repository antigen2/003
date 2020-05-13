# Generated by Django 3.0.4 on 2020-04-01 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0012_auto_20200401_1045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coach',
            options={'ordering': ('last_name', 'first_name', 'middle_name'), 'verbose_name': 'Тренер'},
        ),
        migrations.AlterModelOptions(
            name='gym',
            options={'ordering': ('short_name',), 'verbose_name': 'Спорт. зал'},
        ),
        migrations.AlterModelOptions(
            name='organization',
            options={'ordering': ('short_name',), 'verbose_name': 'Организация'},
        ),
        migrations.AlterField(
            model_name='gym',
            name='address',
            field=models.CharField(max_length=150, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='gym',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Полное наименование'),
        ),
        migrations.AlterField(
            model_name='gym',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='gyms', to='tournament.Organization', verbose_name='Организация'),
        ),
        migrations.AlterField(
            model_name='gym',
            name='short_name',
            field=models.CharField(max_length=100, verbose_name='Сокращенное наименование'),
        ),
        migrations.AlterField(
            model_name='gym',
            name='slug',
            field=models.SlugField(max_length=100, verbose_name='Имя для ссылки'),
        ),
        migrations.AlterField(
            model_name='gym',
            name='status',
            field=models.CharField(choices=[('active', 'Действующий'), ('closed', 'Закрытый')], default='active', max_length=15, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='address',
            field=models.CharField(max_length=150, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Полное наименование'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='short_name',
            field=models.CharField(max_length=50, verbose_name='Сокращенное наименование'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='slug',
            field=models.SlugField(max_length=100, verbose_name='Имя для ссылки'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='status',
            field=models.CharField(choices=[('active', 'Действующая'), ('not_exist', 'Не существует')], default='active', max_length=15, verbose_name='Статус'),
        ),
    ]