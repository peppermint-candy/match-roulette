# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='blocked',
            field=models.ManyToManyField(related_name='_user_blocked_+', to='login_reg.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='user',
            name='favorite',
            field=models.ManyToManyField(related_name='_user_favorite_+', to='login_reg.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='orientation',
            field=models.ManyToManyField(related_name='talks_to', to='login_reg.Gender'),
        ),
    ]
