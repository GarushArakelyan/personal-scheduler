from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns= [
        path('', views.CalendarView.as_view() ,name='turtly-home'),
        path('studies/', views.studies ,name='turtly-studies'),
        path('workout/', views.workout ,name='turtly-workout'),
        path('post/update/<int:pk>/', views.UpdateMe.as_view(), name='post-update'),
        path('post/<int:pk>/', views.DetailMe.as_view(), name='post-detail'),
        path('login/', auth_views.LoginView.as_view(template_name='turtly/login.html'), name='turtly-login'),
        path('workout/<str:days>/', views.particular, name='turtly-workout-detail'),


]