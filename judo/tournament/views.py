from django.shortcuts import render, get_object_or_404
from .models import \
    Organization, Gym, Coach, WeightClass, Judoka, Tournament, \
    Competitor, TournamentTable, TournamentTableGroup
from .models import WeightHistory
from django.views.generic import ListView


# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# def organization_list(request):
#     """
#     Формирует список организаций для постраничного отображения,
#     по 5 на траницу
#     :param request:
#     :return:
#     """
#     object_list = Organization.active.all()
#     paginator = Paginator(object_list, 5) # 5 орг. на стр.
#     page = request.GET.get('page')
#
#     try:
#         organizations = paginator.page(page)
#     except PageNotAnInteger:
#         organizations = paginator.page(1)
#     except EmptyPage:
#         organizations = paginator.page(paginator.num_pages)
#
#     return render(request,
#                   'organization/list.html',
#                   {'page': page, 'organizations': organizations})
class OrganizationListView(ListView):
    """
    Формирует список организаций для постраничного отображения
    4 на страницу
    """
    queryset = Organization.active.all()
    context_object_name = 'organizations'
    paginate_by = 4
    template_name = 'organization/list.html'


def organization_detail(request, organization):
    """
    Возвращаем данные по отдельной организации
    :param request:
    :param organization:
    :return:
    """
    organization = get_object_or_404(Organization, slug=organization,
                                     status='active')
    return render(request,
                  'organization/detail.html',
                  {'organization': organization})


class GymListView(ListView):
    """
    Формирует список спортзалов для постраничного отображения
    4 на страницу
    """
    queryset = Gym.active.all()
    context_object_name = 'gyms'
    paginate_by = 4
    template_name = 'gym/list.html'


def gym_detail(request, gym):
    """
    Возвращаем данные по отдельному спортзалу
    :param request:
    :param gym:
    :return:
    """
    gym = get_object_or_404(Gym, slug=gym, status='active')
    return render(request, 'gym/detail.html', {'gym': gym})


class CoachListView(ListView):
    """
    Формирует список тренеров для постраничного отображения
    4 на страницу
    """
    queryset = Coach.objects.all()
    context_object_name = 'coaches'
    paginate_by = 4
    template_name = 'coach/list.html'


def coach_detail(request, coach):
    """
    Возвращаем данные по отдельному тренеру
    :param request:
    :param coach:
    :return:
    """
    coach = get_object_or_404(Coach, slug=coach)
    return render(request, 'coach/detail.html', {'coach': coach})


class JudokaListView(ListView):
    """
    Формирует список спортсменов для постраничного отображения
    4 на страницу
    """
    queryset = Judoka.active.all()
    context_object_name = 'judokas'
    paginate_by = 4
    template_name = 'judoka/list.html'


def judoka_detail(request, judoka):
    """
    Возвращаем данные по отдельному тренеру
    :param request:
    :param judoka:
    :return:
    """
    judoka = get_object_or_404(Judoka, slug=judoka)
    weight_history = WeightHistory.objects.filter(judoka=judoka).order_by('-date')
    return render(request, 'judoka/detail.html', {'judoka': judoka, 'weight_history': weight_history})


class TournamentListView(ListView):
    """
    Формирует список турниров для постраничного отображения
    4 на страницу
    """
    queryset = Tournament.completed.all()
    context_object_name = 'tournaments'
    paginate_by = 4
    template_name = 'competition/tournament/list.html'


def tournament_detail(request, tournament):
    """
    Возвращаем данные по отдельному турниру
    :param request:
    :param tournament:
    :return:
    """
    tournament = get_object_or_404(Tournament, slug=tournament, status='completed')
    competitors = Competitor.objects.filter(tournament=tournament).order_by('judoka')
    tournament_groups = TournamentTable.objects.filter(tournament=tournament).order_by('weight_class')
    return render(request, 'competition/tournament/detail.html', {
                        'tournament': tournament,
                        'competitors': competitors,
                        'tournament_groups': tournament_groups
                    })


def tournament_table_detail(request, tournament_table):
    """
    Возвращаем данные по определенноу весовой категории турнира
    :param request:
    :param tournament_table:
    :return:
    """
    tournament_table = get_object_or_404(TournamentTable, slug=tournament_table)
    # competitors = Competitor.objects.filter(tournament_table=tournament_table).order_by('')
    return render(request, 'competition/tournament/weight_class/detail.html', {
        'tournament_table': tournament_table,
    })
