# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_friendlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='aboutDream',
            field=models.TextField(null=True, verbose_name='\u5173\u4e8e\u68a6\u60f3', blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='aboutEducation',
            field=models.TextField(null=True, verbose_name='\u5173\u4e8e\u6559\u80b2', blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='aboutLive',
            field=models.TextField(null=True, verbose_name='\u5173\u4e8e\u751f\u6d3b', blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='aboutSkill',
            field=models.TextField(null=True, verbose_name='\u5173\u4e8e\u6280\u80fd', blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='aboutWork',
            field=models.TextField(null=True, verbose_name='\u5173\u4e8e\u5de5\u4f5c', blank=True),
        ),
    ]
