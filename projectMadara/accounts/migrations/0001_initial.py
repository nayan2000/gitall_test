# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-09 16:14
from __future__ import unicode_literals

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=accounts.models.upload_location, width_field='width_field')),
                ('width_field', models.IntegerField(default=0, null=True)),
                ('height_field', models.IntegerField(default=0, null=True)),
                ('bio', models.TextField(blank=True, max_length=60, null=True, verbose_name='You in 60 words.')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, verbose_name='Contact Number')),
                ('status', models.CharField(default='Student', max_length=128)),
                ('totos', models.IntegerField(default=0, verbose_name='Contribution')),
                ('user_since', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='email address')),
                ('custom_link', models.URLField(blank=True, null=True)),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('linkedin_link', models.URLField(blank=True, null=True)),
                ('github_link', models.URLField(blank=True, null=True)),
                ('reddit_link', models.URLField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
