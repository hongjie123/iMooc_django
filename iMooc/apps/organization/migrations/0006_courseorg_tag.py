# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-25 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_teacher_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='tag',
            field=models.CharField(default='全国知名', max_length=50, verbose_name='机构标签'),
        ),
    ]
