# Generated by Django 4.2.3 on 2023-07-26 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends_app', '0008_alter_director_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, default='', upload_to='all_photos_friends/%y/%m/%d', verbose_name='Карточки')),
            ],
        ),
    ]
