# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 11:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poetry', '0003_auto_20170801_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thewords', models.TextField()),
                ('poem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poetry.Poem')),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='linefavorite',
            field=models.ManyToManyField(related_name='line_favorite', to='poetry.Line'),
        ),
    ]
