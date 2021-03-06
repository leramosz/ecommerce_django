# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 14:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('price', models.FloatField()),
                ('sale_off', models.FloatField()),
                ('image', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('hot', models.BooleanField()),
                ('highlighted', models.BooleanField()),
                ('new', models.BooleanField()),
                ('best_seller', models.BooleanField()),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authors.Author')),
            ],
        ),
    ]
