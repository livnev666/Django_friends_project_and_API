# Generated by Django 4.2.3 on 2023-07-26 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends_app', '0013_alter_movie_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='gallery/%y/%m/%d', verbose_name='Фото'),
        ),
    ]
