from django.contrib import admin
from .models import \
    Organization, Gym, Coach, WeightClass, Judoka, Tournament, \
    Competitor, Tatami, TournamentTable, TournamentTableGroup
from .models import WeightHistory


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    # Отображаемые поля
    list_display = ('short_name', 'slug', 'name', 'address')
    # Фильтрация списка (справа)
    # list_filter = ('status', 'short_name', 'name', 'address')
    list_filter = ('status', 'short_name')
    # Строка поиска по полям
    search_fields = ('short_name', 'address')
    # генерация автоматически slug по полю name
    prepopulated_fields = {'slug': ('name', )}
    # сортировка
    ordering = ('status', 'short_name')
    # raw_id_fields = ('short_name', )
    # date_hierarchy = 'поле'


@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'slug', 'name', 'address', 'organization')
    list_filter = ('status', 'short_name', 'organization')
    search_fields = ('short_name', 'address')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('status', 'organization', 'short_name')


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'short_name', 'gym')
    list_filter = ('gym', )
    search_fields = ('short_name', 'gym')
    prepopulated_fields = {'slug': ('gym', 'last_name', 'first_name', 'middle_name')}
    ordering = ('gym', 'short_name')


@admin.register(WeightClass)
class WeightClassAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name', )
    search_fields = ('name', )
    ordering = ('name', )


@admin.register(Judoka)
class JudokaAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'short_name',
                    'birthday', 'gender', 'rating', 'rating_points', 'slug',
                    'coach', 'status', 'pay')
    list_filter = ('coach', 'gender', 'status', 'pay')
    search_fields = ('last_name', 'first_name', 'middle_name', 'short_name')
    prepopulated_fields = {'slug': ('last_name', 'first_name', 'middle_name', 'birthday')}
    ordering = ('short_name', )


@admin.register(WeightHistory)
class WeightHistoryAdmin(admin.ModelAdmin):
    list_display = ('judoka', 'weight_class', 'date')
    list_filter = ('judoka', 'weight_class')
    search_fields = ('judoka', 'weight_class')
    ordering = ('judoka', 'date', 'weight_class')


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'number_of_tatami', 'date', 'slug', 'status')
    list_filter = ('status', 'name', 'date')
    search_fields = ('name', 'shot_name')
    prepopulated_fields = {'slug': ('name', 'date')}
    ordering = ('-date', )


@admin.register(Competitor)
class CompetitorAdmin(admin.ModelAdmin):
    list_display = ('tournament', 'judoka', 'rating_points')
    list_filter = ('tournament', 'judoka')
    search_fields = ('tournament', 'judoka')
    prepopulated_fields = {'slug': ('tournament', 'judoka')}
    ordering = ('tournament', 'judoka')


@admin.register(Tatami)
class TatamiAdmin(admin.ModelAdmin):
    list_display = ('tournament', 'number', 'slug')
    list_filter = ('tournament', )
    search_fields = ('tournament', )
    prepopulated_fields = {'slug': ('tournament', 'number')}
    ordering = ('tournament', 'number')


@admin.register(TournamentTable)
class TournamentTableAdmin(admin.ModelAdmin):
    list_display = ('tournament', 'weight_class', 'competition_system', 'slug')
    list_filter = ('tournament', )
    search_fields = ('tournament', )
    prepopulated_fields = {'slug': ('tournament', 'weight_class')}
    ordering = ('tournament', 'weight_class')


@admin.register(TournamentTableGroup)
class TournamentTableGroupAdmin(admin.ModelAdmin):
    list_display = ('tournament_table', 'group')
    list_filter = ('tournament_table', )
    search_fields = ('tournament_table', )
    prepopulated_fields = {'slug': ('tournament_table', 'group')}
    ordering = ('tournament_table', 'group')
