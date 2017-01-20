# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 15:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import shop.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modification date')),
                ('published', models.BooleanField(default=True, help_text='Decides whether entity should be treated as active.', verbose_name='Published')),
                ('ordering', models.IntegerField(blank=True, default=0, null=True, verbose_name='Ordering')),
                ('slug', models.CharField(default='', max_length=250, unique=True, verbose_name='Slug')),
                ('name', models.CharField(default='', max_length=250, verbose_name='Name')),
                ('title', models.CharField(blank=True, default='', max_length=250, verbose_name='Title')),
                ('description', models.CharField(blank=True, default='', max_length=250, verbose_name='Description')),
                ('keywords', models.CharField(blank=True, default='', max_length=250, verbose_name='Keywords')),
                ('image', models.ImageField(blank=True, default='', upload_to=shop.models.make_upload_path, verbose_name='Image')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='shop.Category', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modification date')),
                ('published', models.BooleanField(default=True, help_text='Decides whether entity should be treated as active.', verbose_name='Published')),
                ('ordering', models.IntegerField(blank=True, default=0, null=True, verbose_name='Ordering')),
                ('image', models.ImageField(blank=True, default='', upload_to=shop.models.make_upload_path, verbose_name='Image')),
                ('name', models.CharField(default='', max_length=250, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modification date')),
                ('published', models.BooleanField(default=True, help_text='Decides whether entity should be treated as active.', verbose_name='Published')),
                ('ordering', models.IntegerField(blank=True, default=0, null=True, verbose_name='Ordering')),
                ('name', models.CharField(default='', max_length=250, verbose_name='Name')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, null=True, verbose_name='Price')),
            ],
            options={
                'verbose_name': 'Offer',
                'verbose_name_plural': 'Offers',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modification date')),
                ('published', models.BooleanField(default=True, help_text='Decides whether entity should be treated as active.', verbose_name='Published')),
                ('ordering', models.IntegerField(blank=True, default=0, null=True, verbose_name='Ordering')),
                ('slug', models.CharField(blank=True, db_index=True, default='', max_length=250, verbose_name='Slug')),
                ('url', models.CharField(blank=True, default='', max_length=250, verbose_name='Url')),
                ('name', models.CharField(default='', max_length=250, verbose_name='Name')),
                ('title', models.CharField(blank=True, default='', max_length=250, verbose_name='Title')),
                ('description', models.CharField(blank=True, default='', max_length=250, verbose_name='Description')),
                ('keywords', models.CharField(blank=True, default='', max_length=250, verbose_name='Keywords')),
                ('image', models.ImageField(blank=True, default='', upload_to=shop.models.make_upload_path, verbose_name='Image')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, null=True, verbose_name='Price')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='shop.Category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.AddField(
            model_name='offer',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='shop.Product', verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='images',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.Product', verbose_name='Product'),
        ),
    ]
