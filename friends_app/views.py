from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.db.models import F, Sum, Max, Min, Count, Avg
from django.views.generic import CreateView, ListView, DetailView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .models import Director, Movie, Actor, Photos, AudioTrack, CommentUser
from django.views.generic import CreateView, ListView
from django.views import View
from .forms import SongsForm, AddPageForm, RegistrationForm, LoginForm, CommentUserForm

from django.views.decorators.cache import cache_page


# Create your views here.

dc_bar = [
    {'title': 'Главная', 'url_name': 'info_tv_series'},
    {'title': 'О сериале', 'url_name': 'about-serial'},
    {'title': 'Актеры', 'url_name': 'actors'},
    {'title': 'Режиссеры сериала Друзья', 'url_name': 'directors_friends'},
    {'title': 'Режиссеры', 'url_name': 'directors'},
    {'title': 'Фото', 'url_name': 'photos'},
    {'title': 'Фильмы с актерами из друзей', 'url_name': 'movies'},
    {'title': 'Саундтрек', 'url_name': 'soundtrack'},
    {'title': 'API', 'url_name': 'api'},

]


class AddInfoView(CreateView):

    model = Movie
    form_class = AddPageForm
    template_name = 'friends_app/add_info.html'
    success_url = '/movies'
    raise_exception = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить информацию'
        context['dc_bar'] = dc_bar
        return context


class AddSoundTrack_View(CreateView):

    model = AudioTrack
    form_class = SongsForm
    template_name = 'friends_app/song_form.html'
    success_url = '/soundtrack'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить трек'
        context['dc_bar'] = dc_bar
        return context
# class SoundTrack(View):
#
#     def get(self, request):
#         form = SongsForm()
#         return render(request, 'friends_app/song_form.html', {'form': form})
#
#     def post(self, request):
#         form = SongsForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_songs = AudioTrack(song=request.FILES['song'])
#             new_songs.save()
#             return HttpResponseRedirect('/soundtrack')
#         return render(request, 'friends_app/song_form.html', {'form': form})

###################################################################################################

class AboutSerial(ListView):

    model = Movie
    template_name = 'friends_app/about_serial.html'
    context_object_name = 'mov'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'mov': Movie.objects.get(id=1),
            'dc_bar': dc_bar
        })
        return context

# class MainPage(ListView):
#
#     model = Actor
#     template_name = 'friends_app/main_page.html'
#     context_object_name = 'post'
#     allow_empty = False
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context.update({
#             'post': Actor.objects.all()[:6],
#             'mov': Movie.objects.get(id=1),
#             'dc_bar': dc_bar
#         })
#         return context
def main_page(request):

    data = {
        'dc_bar': dc_bar
    }
    return render(request, 'friends_app/main_page.html', context=data)

############################################################################################


class SoundtrackOfFriends(LoginRequiredMixin, ListView):

    model = AudioTrack
    template_name = 'friends_app/soundtrack_of_friends.html'
    context_object_name = 'sound'
    login_url = reverse_lazy('log-in')
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Саундтреки к сериалу Друзья'
        context['dc_bar'] = dc_bar
        return context
# def soundtrack_of_friends(request):
#
#     sound = AudioTrack.objects.all()
#     data = {
#         'title': 'Саундтреки к сериалу Друзья',
#         'sound': sound,
#         'dc_bar': dc_bar,
#     }
#     return render(request, 'friends_app/soundtrack_of_friends.html', context=data)
#########################################################################################################
#############################################################################################


class ListActors(ListView):

    model = Actor
    template_name = 'friends_app/list_actors.html'
    context_object_name = 'post'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список актеров'
        context['dc_bar'] = dc_bar
        return context
# def list_actors(request):
#
#     post = Actor.objects.all()
#     data = {
#         'title': 'Список актеров',
#         'post': post,
#         'dc_bar': dc_bar
#     }
#     return render(request, 'friends_app/list_actors.html', context=data)


class OneActor(DetailView):

    model = Actor
    template_name = 'friends_app/one_actor.html'
    context_object_name = 'one_actor'
    slug_url_kwarg = 'slug_actor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dc_bar'] = dc_bar
        return context
# def one_actor(request, slug_actor: str):
#
#     one_actor = Actor.objects.get(slug=slug_actor)
#     data = {
#         'one_actor': one_actor,
#         'dc_bar': dc_bar
#     }
#     return render(request, 'friends_app/one_actor.html', context=data)

###################################################################################################
####################################################################################################


class AllDirectorFriends(ListView):

    model = Director
    template_name = 'friends_app/list_directors_friends.html'
    context_object_name = 'dir'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'dir': Director.objects.all()[:3],
            'title': 'Список режиссеров сериала Друзья',
            'dc_bar': dc_bar
        })
        return context
# def all_directors_friends(request):
#
#     director = Director.objects.all()
#     data = {
#         'dir': director[:3],
#         'title': 'Список режиссеров',
#         'dc_bar': dc_bar,
#     }
#     return render(request, 'friends_app/list_directors_friends.html', context=data)


class AllDirector(ListView):

    model = Director
    template_name = 'friends_app/list_directors.html'
    context_object_name = 'dir'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'dir': Director.objects.all()[3:],
            'title': 'Список режиссеров',
            'agg': Director.objects.all()[3:].aggregate(Max('age'), Min('age')),
            'dc_bar': dc_bar,
        })
        return context
# def all_directors(request):
#
#     director = Director.objects.all()
#     data = {
#         'dir': director[3:],
#         'title': 'Список режиссеров',
#         'dc_bar': dc_bar,
#     }
#     return render(request, 'friends_app/list_directors.html', context=data)


class OneDirector(DetailView):

    model = Director
    template_name = 'friends_app/one_director.html'
    context_object_name = 'one_dir'
    slug_url_kwarg = 'slug_dir'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dc_bar'] = dc_bar
        return context
# def one_director(request, slug_dir: str):
#
#     dir = Director.objects.get(slug=slug_dir)
#     data = {
#         'one_dir': dir,
#         'dc_bar': dc_bar
#     }
#     return render(request, 'friends_app/one_director.html', context=data)

#############################################################################################################
############################################################################################################


class Photos(ListView):

    model = Photos
    template_name = 'friends_app/photos.html'
    context_object_name = 'ph'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Фотографии',
            'dc_bar': dc_bar
        })
        return context
# def photos(request):
#
#     ph = Photos.objects.all()
#     data = {
#         'ph': ph,
#         'dc_bar': dc_bar,
#         'title': 'Фотографии'
#     }
#     return render(request, 'friends_app/photos.html', context=data)

#########################################################################################################
######################################################################################################


class Movies(ListView):

    model = Movie
    template_name = 'friends_app/list_movies.html'
    context_object_name = 'mov'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Список фильмов с актерами из Друзей',
            'dc_bar': dc_bar,
            'agg': Movie.objects.all().aggregate(Count('id'))
        })
        return context
# def movies(request):
#
#     mov = Movie.objects.all()
#     data = {
#         'mov': mov,
#         'title': 'Список фильмов с актерами из Друзей',
#         'dc_bar': dc_bar,
#     }
#     return render(request, 'friends_app/list_movies.html', context=data)


class OneMovie(DetailView):

    model = Movie
    template_name = 'friends_app/one_movie.html'
    context_object_name = 'one_mov'
    slug_url_kwarg = 'slug_movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dc_bar'] = dc_bar
        return context
# def one_movie(request, slug_movie: str):
#
#     mov = Movie.objects.get(slug=slug_movie)
#     data = {
#         'one_mov': mov,
#         'dc_bar': dc_bar
#     }
#     return render(request, 'friends_app/one_movie.html', context=data)
#####################################################################################################


class RegistrationView(CreateView):

    form_class = RegistrationForm
    template_name = 'friends_app/registration.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        context['dc_bar'] = dc_bar
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('info_tv_series')


class LoginViews(LoginView):

    form_class = LoginForm
    template_name = 'friends_app/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        context['dc_bar'] = dc_bar
        return context

    def get_success_url(self):
        return reverse('info_tv_series')


def log_out_user(request):
    logout(request)
    return redirect('log-in')

def rest_api(request):

    data = {
        'dc_bar': dc_bar
    }
    return render(request, 'friends_app/API.html', context=data)


class AddCommentUser(CreateView):

    model = CommentUser
    form_class = CommentUserForm
    template_name = 'friends_app/add_comment.html'
    success_url = '/comment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить интересный факт из сериала Друзья'
        context['dc_bar'] = dc_bar
        return context


class AllCommentUser(ListView):

    model = CommentUser
    template_name = 'friends_app/user_comment.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Комментарии к сериалу Друзья'
        context['dc_bar'] = dc_bar
        return context
# def all_comment_user(request):
#
#     post = CommentUser.objects.all()
#     data = {
#         'title': 'Комментарии',
#         'dc_bar': dc_bar,
#         'post': post
#     }
#     return render(request, 'friends_app/user_comment.html', context=data)


'''# Когда пока нет еще slug
#<h2><a href="{% url 'one_dir' sign_number=i.id%}">{{i.first_name}} {{i.last_name}}</a></h2>

# <h3>Информация о режиссере</h3>
#     <p>Имя: {{one_mov.director.first_name}}</p>
#     <p>Фамилия: <a href="{% url 'one_dir' sign_number=one_mov.director.id %}">{{one_mov.director.last_name}}</a></p>
#     <p>Биография: {{one_mov.director.content}}</p>'''
