# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-14 14:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wiki', models.CharField(max_length=20000)),
                ('title', models.CharField(max_length=20000, unique=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('resource', models.TextField(max_length=20000)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Wiki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField(blank=True, max_length=20000, null=True)),
                ('history', models.TextField(blank=True, max_length=20000, null=True)),
                ('features', models.TextField(blank=True, max_length=20000, null=True)),
                ('version_history', models.TextField(blank=True, max_length=20000, null=True)),
                ('url', models.TextField(blank=True, max_length=5000, null=True)),
                ('tech_name', models.CharField(blank=True, max_length=100, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('eli', models.TextField(blank=True, max_length=20000, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('tags', models.ManyToManyField(blank=True, related_name='wiki_pages', to='tags.Tag')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp', '-last_updated'],
            },
        ),
    ]
