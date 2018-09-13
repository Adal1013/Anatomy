# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('imagen', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Parte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('organo', models.ForeignKey(to='digital.Organo')),
            ],
        ),
    ]
