# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20151109_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='someWord',
            field=models.TextField(null=True, verbose_name='\u60f3\u8bf4\u7684\u8bdd', blank=True),
        ),
    ]
