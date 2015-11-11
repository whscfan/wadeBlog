# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'\xe9\xbb\x98\xe8\xae\xa4\xe5\x88\x86\xe7\xb1\xbb', unique=True, max_length=255, verbose_name='\u5206\u7c7b')),
                ('parent', models.ForeignKey(verbose_name='\u7236\u5206\u7c7b', blank=True, to='blog.Category', null=True)),
            ],
            options={
                'ordering': ['-name'],
                'db_table': 'category',
            },
        ),
    ]
