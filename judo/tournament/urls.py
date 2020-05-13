from django.urls import path
from . import views


app_name = 'tournament'

urlpatterns = [
    # path('organization/', views.organization_list,
    #      name='organization_list'),
    path('organization/', views.OrganizationListView.as_view(),
         name='organization_list'),
    path('organization/<slug:organization>/', views.organization_detail,
         name='organization_detail'),
    path('gym/', views.GymListView.as_view(), name='gym_list'),
    path('gym/<slug:gym>/', views.gym_detail, name='gym_detail'),
    path('coach/', views.CoachListView.as_view(), name='coach_list'),
    path('coach/<slug:coach>/', views.coach_detail, name='coach_detail'),
    path('judoka/', views.JudokaListView.as_view(), name='judoka_list'),
    path('judoka/<slug:judoka>/', views.judoka_detail, name='judoka_detail'),
    path('competition/tournament/', views.TournamentListView.as_view(),
         name='tournament_list'),
    path('competition/tournament/<slug:tournament>/', views.tournament_detail,
         name='tournament_detail'),
]
