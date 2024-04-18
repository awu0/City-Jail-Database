from django.urls import path

from jail.views import views
from jail.views import criminal_views, alias_views, crime_views, probation_officer_views, sentence_views, \
    crime_code_views, crime_charge, officer_views

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
    path('crime/<int:pk>/', crime_views.CrimeDetailView.as_view(), name='crime_detail'),
    path('crime/<int:pk>/update/', crime_views.CrimeUpdateView.as_view(), name='crime_update'),
    path('crime/add/', crime_views.CrimeFormView.as_view(), name='crime_add'),
    path('crime/<int:pk>/delete/', crime_views.CrimeDeleteView.as_view(), name='crime_delete'),

    # probation officer paths
    path('probation_officer/', probation_officer_views.ProbationOfficerHomeView.as_view(),
         name='probation_officer_home'),
    path('probation_officer/<int:pk>/', probation_officer_views.ProbationOfficerDetailView.as_view(),
         name='probation_officer_detail'),
    path('probation_officer/<int:pk>/update', probation_officer_views.ProbationOfficerUpdateView.as_view(),
         name='probation_officer_update'),
    path('probation_officer/add/', probation_officer_views.ProbationOfficerFormView.as_view(),
         name='probation_officer_add'),
    path('probation_officer/<int:pk>/delete', probation_officer_views.ProbationOfficerDeleteView.as_view(),
         name='probation_officer_delete'),

    # sentence paths
    path('sentence/', sentence_views.SentenceHomeView.as_view(), name='sentence_home'),
    path('sentence/<int:pk>/update/', sentence_views.SentenceUpdateView.as_view(), name='sentence_update'),
    path('sentence/add/', sentence_views.SentenceFormView.as_view(), name='sentence_add'),
    path('sentence/<int:pk>/delete/', sentence_views.SentenceDeleteView.as_view(), name='sentence_delete'),

    # crime code paths
    path('crime_code/', crime_code_views.CrimeCodeHomeView.as_view(), name='crime_code_home'),
    path('crime_code/<int:pk>/', crime_code_views.CrimeCodeDetailView.as_view(), name='crime_code_detail'),
    path('crime_code/<int:pk>/update/', crime_code_views.CrimeCodeUpdateView.as_view(), name='crime_code_update'),
    path('crime_code/add/', crime_code_views.CrimeCodeFormView.as_view(), name='crime_code_add'),
    path('crime_code/<int:pk>/delete/', crime_code_views.CrimeCodeDeleteView.as_view(), name='crime_code_delete'),

    # crime charge paths
    path('crime_charge/', crime_charge.CrimeChargeHomeView.as_view(), name='crime_charge_home'),
    path('crime_charge/<int:pk>/update/', crime_charge.CrimeChargeUpdateView.as_view(), name='crime_charge_update'),
    path('crime_charge/add/', crime_charge.CrimeChargeFormView.as_view(), name='crime_charge_add'),
    path('crime_charge/<int:pk>/delete/', crime_charge.CrimeChargeeDeleteView.as_view(), name='crime_charge_delete'),

    # officer paths
    path('officer/', officer_views.OfficerHomeView.as_view(), name='officer_home'),
    path('officer/<int:pk>/', officer_views.OfficerDetailView.as_view(), name='officer_detail'),
    path('officer/<int:pk>/update/', officer_views.OfficerUpdateView.as_view(), name='officer_update'),
    path('officer/add/', officer_views.OfficerFormView.as_view(), name='officer_add'),
    path('officer/<int:pk>/delete/', officer_views.OfficerDeleteView.as_view(), name='officer_delete'),
]
