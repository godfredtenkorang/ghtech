# Generated by Django 5.1 on 2024-09-04 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='team-img')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('facebook_link', models.URLField()),
                ('instagram_link', models.URLField()),
                ('tiktok_link', models.URLField()),
                ('github_link', models.URLField()),
                ('website_link', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Our Team',
            },
        ),
    ]
