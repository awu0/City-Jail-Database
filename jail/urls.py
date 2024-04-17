from django.urls import path

from jail.views import views
from jail.views import criminal_views

urlpatterns = [
    # home paths
    path('', views.IndexView.as_view(), name='site_home'),

    # criminal paths
    path('criminal/', criminal_views.CriminalHomeView.as_view(), name='criminal_home'),
    path('criminal/<int:pk>/', criminal_views.CriminalDetailView.as_view(), name='criminal_detail'),
    path('criminal/<int:pk>/update/', criminal_views.CriminalUpdateView.as_view(), name='criminal_update'),
    path('criminal/add/', criminal_views.CriminalFormView.as_view(), name='criminal_add'),
    path('criminal/<int:pk>/delete/', criminal_views.CriminalDeleteView.as_view(), name='criminal_delete'),

    # alias paths
    path('alias/', criminal_views.CriminalHomeView.as_view(), name='alias_home')
]
