# Generated by Django 5.1 on 2024-08-31 16:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='HomeBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='homeblog_img')),
                ('profile_image', models.ImageField(upload_to='profile_img')),
                ('slug', models.SlugField(unique=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.article')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Home Blogs',
            },
        ),
    ]
