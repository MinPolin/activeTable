# Generated by Django 3.0.4 on 2021-04-21 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_id', models.CharField(max_length=64)),
                ('fon_id', models.CharField(max_length=200)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('error_text', models.TextField(default='')),
                ('status', models.CharField(choices=[('w', 'Ожидает отправки'), ('d', 'Отправлен'), ('s', 'Успешно сохранен'), ('e', 'Ошибка')], default='w', help_text='Статус записи', max_length=1)),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Хранилище записей',
            },
        ),
    ]