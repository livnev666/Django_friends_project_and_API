# Generated by Django 4.2.3 on 2023-07-25 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends_app', '0007_alter_actor_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='gallery/%y/%m/%d', verbose_name='Фото'),
        ),
    ]
