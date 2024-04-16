from django.urls import path

from . import views

urlpatterns = [
    # home paths
    path('', views.index, name='index'),

    # criminal paths
    path('criminal', views.criminal_home, name='criminal_home'),
    path('criminal/<int:criminal_id>/', views.criminal_detail, name='criminal_detail')
]