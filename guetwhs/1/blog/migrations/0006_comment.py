# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20151107_1744'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name='\u7559\u8a00\u5185\u5bb9')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('user', models.CharField(default=b'\xe5\x8c\xbf\xe5\x90\x8d\xe7\x94\xa8\xe6\x88\xb7', max_length=255, verbose_name='\u7528\u6237')),
                ('email', models.CharField(max_length=255, verbose_name='\u90ae\u7bb1', blank=True)),
                ('article', models.ForeignKey(to='blog.Article', blank=True)),
                ('pip', models.ForeignKey(verbose_name='\u7236ID', blank=True, to='blog.Comment', null=True)),
            ],
            options={
                'ordering': ['created'],
                'db_table': 'comment',
            },
        ),
    ]
