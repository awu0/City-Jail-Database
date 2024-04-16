from django.urls import path

from . import views

urlpatterns = [
    # home paths
    path('', views.index, name='index'),

    # criminal paths
    path('criminal', views.CriminalHomeView.as_view(), name='criminal_home'),
    path('criminal/<int:pk>/', views.CriminalDetailView.as_view(), name='criminal_detail'),
    path('criminal/add/', views.CriminalFormView.as_view(), name='criminal_add')
]