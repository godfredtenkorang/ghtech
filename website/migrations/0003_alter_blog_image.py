# Generated by Django 5.1 on 2024-09-01 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='blog_img'),
        ),
    ]
