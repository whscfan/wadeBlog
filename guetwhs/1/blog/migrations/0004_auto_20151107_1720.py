# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20151107_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='account',
            field=models.ForeignKey(default=1, verbose_name='\u4f5c\u8005', to=settings.AUTH_USER_MODEL),
        ),
    ]
