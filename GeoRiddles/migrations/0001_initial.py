# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-13 20:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mystery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('gc_code', models.CharField(max_length=16)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=64)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=8, null=True)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=8, null=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Mysterki',
                'verbose_name': 'Mystery Cache',
            },
        ),
    ]