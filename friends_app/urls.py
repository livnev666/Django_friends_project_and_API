from django.urls import path
from friends_app import views as views_friends


urlpatterns = [

    path('', views_friends.main_page, name='info_tv_series'),
    path('aboutserial', views_friends.AboutSerial.as_view(), name='about-serial'),
    path('addcomment/', views_friends.AddCommentUser.as_view(), name='add-comment-user'),
    path('comment/', views_friends.AllCommentUser.as_view(), name='comment-user'),
    path('registration/', views_friends.RegistrationView.as_view(), name='registr'),
    path('login/', views_friends.LoginViews.as_view(), name='log-in'),
    path('formtrack/', views_friends.AddSoundTrack_View.as_view(), name='add_track'),
    path('soundtrack/', views_friends.SoundtrackOfFriends.as_view(), name='soundtrack'),
    path('actors/', views_friends.ListActors.as_view(), name='actors'),
    path('about/<slug:slug_actor>/', views_friends.OneActor.as_view(), name='one_actor'),
    path('dirfriends/', views_friends.AllDirectorFriends.as_view(), name='directors_friends'),
    path('directors/', views_friends.AllDirector.as_view(), name='directors'),
    path('aboutdir/<slug:slug_dir>/', views_friends.OneDirector.as_view(), name='one_dir'),
    path('photos/', views_friends.Photos.as_view(), name='photos'),
    path('movies/', views_friends.Movies.as_view(), name='movies'),
    path('movie/<slug:slug_movie>/', views_friends.OneMovie.as_view(), name='one_movie'),
    path('addinfo/', views_friends.AddInfoView.as_view(), name='add_info'),
    path('logout/', views_friends.log_out_user, name='log-out'),
    path('api/', views_friends.rest_api, name='api'),



]