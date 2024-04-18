from django.urls import path

from jail.views import views
from jail.views import criminal_views, alias_views, crime_views

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
    path('alias/', alias_views.AliasHomeView.as_view(), name='alias_home'),
    path('alias/<int:pk>/update/', alias_views.AliasUpdateView.as_view(), name='alias_update'),
    path('alias/add/', alias_views.AliasFormView.as_view(), name='alias_add'),
    path('alias/<int:pk>/delete/', alias_views.AliasDeleteView.as_view(), name='alias_delete'),

    # crime paths
    path('crime/', crime_views.CrimeHomeView.as_view(), name='crime_home'),
    path('crime/<int:pk>/update/', crime_views.CrimeUpdateView.as_view(), name='crime_update'),
    path('crime/add/', crime_views.CrimeFormView.as_view(), name='crime_add'),
    path('crime/<int:pk>/delete/', crime_views.CrimeDeleteView.as_view(), name='crime_delete'),
]
