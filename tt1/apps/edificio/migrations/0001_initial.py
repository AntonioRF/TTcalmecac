# Generated by Django 2.0.2 on 2018-04-01 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('nivel', models.IntegerField()),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
    ]
