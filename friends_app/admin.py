from django.contrib import admin
from django.contrib import admin, messages
from .models import Movie, Director, Actor, Photos
from django.db.models import QuerySet
from django.utils.safestring import mark_safe
# Register your models here.


class CategoryFilter(admin.SimpleListFilter):

    title = 'Фильтр по категориям'
    parameter_name = 'категории'

    def lookups(self, request, model_admin):
        return [
            ('боевики', 'Боевики'),
            ('комедии', 'Комедии'),
            ('мелодрамы', 'Мелодрамы'),
            ('триллеры', 'Триллеры')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == 'боевики':
            return queryset.filter(id__in=[5, 10, 12])
        if self.value() == 'комедии':
            return queryset.filter(id__in=[1, 4, 7, 8, 9, 16, 20])
        if self.value() == 'мелодрамы':
            return queryset.filter(id__in=[3, 6, 11, 15, 23])
        if self.value() == 'триллеры':
            return queryset.filter(id__in=[2, 13, 14])
        return queryset


class RatingFilter(admin.SimpleListFilter):

    title = 'Фильтр по рейтингу'
    parameter_name = 'рейтинг'

    def lookups(self, request, model_admin):
        return [
            ('< 3', 'Низкий'),
            ('от 3 до 5', 'Средний'),
            ('от 6 до 8', 'Высокий'),
            ('выше 8', 'ТОП фильм')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '< 3':
            return queryset.filter(rating__lt=3)
        if self.value() == 'от 3 до 5':
            return queryset.filter(rating__gte=3).filter(rating__lt=6)
        if self.value() == 'от 6 до 8':
            return queryset.filter(rating__gt=5).filter(rating__lt=9)
        if self.value() == 'выше 8':
            return queryset.filter(rating__gt=8)
        return queryset


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'content', 'image_photo_directors']
    list_display_links = ['first_name', 'last_name']
    list_per_page = 5
    ordering = ['id']
    prepopulated_fields = {'slug': ('first_name',)}

    def image_photo_directors(self, obj):
        if obj.photo:
            return mark_safe("<img src='{}' width='60'/>".format(obj.photo.url))
    image_photo_directors.__name__ = 'Фотокарточка'


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'content', 'image_photo_actors', 'is_published', 'link_web']
    list_display_links = ['first_name', 'last_name']
    list_per_page = 5
    ordering = ['id']
    prepopulated_fields = {'slug': ('first_name', )}

    def image_photo_actors(self, obj):
        if obj.photo:
            return mark_safe("<img src='{}' width='60'/>".format(obj.photo.url))
    image_photo_actors.__name__ = 'Фотокарточка'


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'years', 'content', 'rating', 'director']
    list_display_links = ['name', 'director']
    list_per_page = 5
    list_filter = [CategoryFilter, RatingFilter]
    filter_horizontal = ['actors']
    ordering = ['id']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):

    list_display = ['id', 'image_photo']
    ordering = ['id']

    def image_photo(self, obj):
        if obj.photo:
            return mark_safe("<img src='{}' width='60'/>".format(obj.photo.url))
    image_photo.__name__ = 'Фотокарточка'



