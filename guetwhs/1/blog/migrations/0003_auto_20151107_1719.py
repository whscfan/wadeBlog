# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(null=True, verbose_name='\u6587\u7ae0\u6807\u9898', blank=True)),
                ('content', models.TextField(null=True, verbose_name='\u6587\u7ae0\u5185\u5bb9', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('lastModify', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u4fee\u6539\u65f6\u95f4')),
                ('tag', models.TextField(default='\u9ed8\u8ba4\u6807\u7b7e', verbose_name='\u6807\u7b7e')),
                ('views', models.IntegerField(default=0, verbose_name='\u6d4f\u89c8\u91cf')),
                ('account', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
                'db_table': 'article',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(default=b'1', to='blog.Category', verbose_name='\u5206\u7c7b'),
        ),
    ]
