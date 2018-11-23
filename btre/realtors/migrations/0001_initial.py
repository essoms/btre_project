# Generated by Django 2.1.3 on 2018-11-17 11:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('description', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=15)),
                ('is_mvp', models.BooleanField(default=True)),
                ('hire_data', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
