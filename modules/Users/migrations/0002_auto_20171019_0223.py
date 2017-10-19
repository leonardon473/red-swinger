# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 02:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.Country'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id_cover_photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.Cover_photo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id_profile_photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.Profile_photo'),
        ),
    ]
