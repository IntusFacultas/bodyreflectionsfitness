# Generated by Django 3.0.4 on 2020-03-27 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('link', models.URLField(verbose_name='URL')),
            ],
        ),
    ]
