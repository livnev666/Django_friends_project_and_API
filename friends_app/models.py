from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.


class AudioTrack(models.Model):

    name_song = models.CharField(max_length=50, default='', null=False, blank=True, verbose_name='Название трека')
    artist = models.CharField(max_length=50, default='', null=False, blank=True, verbose_name='Исполнитель')
    song = models.FileField(upload_to='sound_track_in_friends/%y/%m/%d', blank=True, default='', null=False, verbose_name='Композиция')

    def __str__(self):
        return f'{self.name_song} {self.artist}'


class Photos(models.Model):

    photo = models.ImageField(upload_to='all_photos_friends/%y/%m/%d', blank=True, default='', null=False, verbose_name='Карточки')

    class Meta:
        verbose_name = 'Фотокарточки'
        verbose_name_plural = 'Фотокарточки'


class Director(models.Model):

    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    age = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name='Возраст')
    content = models.TextField(blank=True, verbose_name='Биография')
    photo = models.ImageField(upload_to='gallery/%y/%m/%d', blank=True, default='', null=False, verbose_name='Фото')
    slug = models.SlugField(max_length=100, default='', null=False, db_index=True, verbose_name='URL')

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.age}'

    def get_director_url(self):
        return reverse('one_dir', kwargs={'slug_dir': self.slug})

    class Meta:
        verbose_name = 'Режиссеры'
        verbose_name_plural = 'Режиссеры'


class Actor(models.Model):

    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    content = models.TextField(blank=True, verbose_name='Биография')
    age = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name='Возраст')
    photo = models.ImageField(upload_to='gallery/%y/%m/%d', default='', null=False, verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    link_web = models.CharField(max_length=255, blank=True, verbose_name='Web ссылка')
    slug = models.SlugField(max_length=100, default='', null=False, db_index=True, verbose_name='URL')

    def __str__(self):
        return f'{self.first_name}{self.last_name} {self.age} {self.photo} {self.is_published} {self.link_web}'

    def get_actor_url(self):
        return reverse('one_actor', kwargs={'slug_actor': self.slug})

    class Meta:
        verbose_name = 'Актеры'
        verbose_name_plural = 'Актеры'


class Movie(models.Model):

    name = models.CharField(max_length=40, verbose_name='Название фильма')
    years = models.IntegerField(blank=True, null=True, verbose_name='Год производства')
    content = models.TextField(blank=True, verbose_name='Описание')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], verbose_name='Рэйтинг')
    photo = models.ImageField(upload_to='gallery/%y/%m/%d', default='', null=False, verbose_name='Фото', blank=True)
    slug = models.SlugField(max_length=100, default='', null=False, db_index=True, verbose_name='URL')

    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, blank=True)
    actors = models.ManyToManyField(Actor)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Пользователь')

    def __str__(self):
        return f'{self.name} {self.years} {self.content} {self.rating}'

    def get_movie_url(self):
        return reverse('one_movie', kwargs={'slug_movie': self.slug})

    class Meta:
        verbose_name = 'Фильмы'
        verbose_name_plural = 'Фильмы'


class CommentUser(models.Model):

    name = models.CharField(max_length=40, verbose_name='Имя пользователя')
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'






