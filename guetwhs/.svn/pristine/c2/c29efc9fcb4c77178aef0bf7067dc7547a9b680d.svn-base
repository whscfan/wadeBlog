# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='friendLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.TextField(verbose_name='\u94fe\u63a5')),
                ('title', models.CharField(max_length=255)),
                ('img', models.TextField(null=True, verbose_name='\u56fe\u7247\u94fe\u63a5', blank=True)),
            ],
            options={
                'db_table': 'friendlink',
            },
        ),
    ]
