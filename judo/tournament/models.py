from django.db import models
from django.utils import timezone
from django.urls import reverse
from datetime import datetime, date


class ActiveOrganizationManager(models.Manager):
    """
    Модель менеджера для организаций
    status='active'
    """
    def get_queryset(self):
        return super().get_queryset().filter(status='active')


class Organization(models.Model):
    """
    Модель организаций
    """
    STATUS_CHOICES = (
        ('active', 'Действующая'),
        ('not_exist', 'Не существует'),
    )
    name = models.CharField(verbose_name='Полное наименование', max_length=100, unique=True)
    short_name = models.CharField(verbose_name='Сокращенное наименование', max_length=50)
    address = models.CharField(verbose_name='Адрес', max_length=150)
    # slug = models.SlugField(max_length=100, unique_for_date=str(timezone.now)
    slug = models.SlugField(verbose_name='Алиас', max_length=100)
    status = models.CharField(
        verbose_name='Статус',
        max_length=15,
        choices=STATUS_CHOICES,
        default='active'
    )
    # Менеджер модели по умолчанию
    objects = models.Manager()
    # Новый менеджер (все активные орг.)
    active = ActiveOrganizationManager()

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ('short_name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tournament:organization_detail',
                       args=[self.slug])


class ActiveGymManager(models.Manager):
    """
    Модель менеджера для организаций
    status='active'
    """
    def get_queryset(self):
        return super().get_queryset().filter(status='active')


class Gym(models.Model):
    """
    Модель спортивных залов
    """
    STATUS_CHOICES = (
        ('active', 'Действующий'),
        ('closed', 'Закрытый'),
    )
    organization = models.ForeignKey(Organization,
                                     verbose_name='Организация',
                                     on_delete=models.PROTECT,
                                     related_name='gyms')
    name = models.CharField(verbose_name='Полное наименование', max_length=100, unique=True)
    short_name = models.CharField(verbose_name='Сокращенное наименование', max_length=100)
    address = models.CharField(verbose_name='Адрес', max_length=150)
    slug = models.SlugField(verbose_name='Алиас', max_length=100)
    status = models.CharField(
        verbose_name='Статус',
        max_length=15,
        choices=STATUS_CHOICES,
        default='active'
    )
    objects = models.Manager()
    active = ActiveGymManager()

    class Meta:
        verbose_name = 'Спорт. зал'
        verbose_name_plural = 'Спорт. залы'
        ordering = ('short_name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tournament:gym_detail',
                       args=[self.slug])


class Coach(models.Model):
    """
    Модель тренеров
    """
    last_name = models.CharField(verbose_name='Фамилия', max_length=25)  # Ф
    first_name = models.CharField(verbose_name='Имя', max_length=25)  # И
    middle_name = models.CharField(verbose_name='Отчество', max_length=25)  # О
    short_name = models.CharField(verbose_name='Фамилия и инициалы', max_length=25)
    slug = models.SlugField(verbose_name='Алиас', max_length=250)
    gym = models.ForeignKey(Gym,
                            verbose_name='Спортивный зал',
                            on_delete=models.PROTECT,
                            related_name='coaches')
    objects = models.Manager()

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'
        ordering = ('last_name', 'first_name', 'middle_name',)

    def __str__(self):
        return self.short_name

    def get_absolute_url(self):
        return reverse('tournament:coach_detail',
                       args=[self.slug])


class WeightClass(models.Model):
    """
    Модель весовых категорий
    """
    name = models.CharField(verbose_name='Наименование весовой категории', max_length=200)
    objects = models.Manager()

    class Meta:
        verbose_name = 'Весовая котегория'
        verbose_name_plural = 'Весовые котегории'
        ordering = ('name', )

    def __str__(self):
        return self.name


class ActiveJudokaManager(models.Manager):
    """
    Модель менеджера для дзюдоистов
    status='active'
    """
    def get_queryset(self):
        return super().get_queryset().filter(status='active')


class Judoka(models.Model):
    """
    Модель дзюдоиста
    """
    STATUS_CHOICES = (
        ('active', 'Тренеруется'),
        ('not_active', 'Не тренеруется'),
    )
    PAY_STATUS = (
        ('payed', 'Оплачено'),
        ('not_payed', 'Не оплачено')
    )
    GENDER_CHOICES = (
        ('male', 'Муж'),
        ('female', 'Жен'),
    )
    last_name = models.CharField(verbose_name='Фамилия', max_length=25)
    first_name = models.CharField(verbose_name='Имя', max_length=25)
    middle_name = models.CharField(verbose_name='Отчество', max_length=25)
    short_name = models.CharField(verbose_name='Фамилия и инициалы', max_length=25)
    birthday = models.DateField(verbose_name='Дата рождения')
    gender = models.CharField(verbose_name='Пол',
                              max_length=6,
                              choices=GENDER_CHOICES,
                              default='male')
    # weight = models.DecimalField(verbose_name='Вес, kg', max_digits=5, decimal_places=2)
    rating = models.IntegerField(verbose_name='Рейтинг', default=0)
    rating_points = models.IntegerField(verbose_name='Очки рейтинга', default=0)
    slug = models.SlugField(verbose_name='Алиас', max_length=250)
    coach = models.ForeignKey(Coach,
                              verbose_name='Тренер',
                              on_delete=models.PROTECT,
                              related_name='judokas')
    status = models.CharField(verbose_name='Действующий спортсмен',
                              max_length=10,
                              choices=STATUS_CHOICES,
                              default='active')
    pay = models.CharField(verbose_name='Орг. взнос',
                           max_length=9,
                           choices=PAY_STATUS,
                           default='not_payed')
    objects = models.Manager()
    active = ActiveJudokaManager()

    class Meta:
        verbose_name = 'Спортсмен'
        verbose_name_plural = 'Спортсмены'
        ordering = ('last_name', 'first_name', 'middle_name',)

    def __str__(self):
        return self.short_name

    def get_absolute_url(self):
        return reverse('tournament:judoka_detail',
                       args=[self.slug])

    def get_full_age(self):
        today = date.today()
        born = self.birthday
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


class WeightHistory(models.Model):
    """
    Модель историй весовых категорий спортсмена
    """
    judoka = models.ForeignKey(Judoka,
                               verbose_name='Спортсмен',
                               on_delete=models.CASCADE,
                               related_name='weight_histories')
    weight_class = models.ForeignKey(WeightClass,
                                     verbose_name='Весовая категория',
                                     on_delete=models.PROTECT,
                                     related_name='weight_classes')
    date = models.DateField(verbose_name='Дата первого выступления в данной весовой категории',
                            auto_now_add=True if None else False)
    objects = models.Manager()

    class Meta:
        verbose_name = 'История весовых категорий'
        verbose_name_plural = 'Истории весовых категорий'
        ordering = ('judoka', 'date')


#                                   Моделирование турнира


class TournamentManager(models.Manager):
    """
    Модель менеджера турниров
    status = 'completed'
    """
    def get_queryset(self):
        return super().get_queryset().filter(status='completed')


class Tournament(models.Model):
    """
    Модель турнира
    """
    STATUS_CHOICES = (
        ('completed', 'Завершенный'),
        ('during', 'В процессе')
    )
    name = models.CharField(verbose_name='Наименование соревнования', max_length=250)
    short_name = models.CharField(verbose_name='Сокращенное название', max_length=100)
    number_of_tatami = models.IntegerField(verbose_name='Количество татами', default=1)
    date = models.DateField(verbose_name='Дата проведения') #, auto_now_add=True)
    slug = models.SlugField(verbose_name='Алиас', max_length=250)
    status = models.CharField(verbose_name='Статус турнира',
                              max_length=9,
                              choices=STATUS_CHOICES,
                              default='during')
    objects = models.Manager()
    completed = TournamentManager()

    class Meta:
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'
        ordering = ('-date', )

    def __str__(self):
        return self.short_name

    def get_absolute_url(self):
        return reverse('tournament:tournament_detail',
                       args=[self.slug])


class Competitor(models.Model):
    """
    Модель участников турнира
    """
    tournament = models.ForeignKey(Tournament,
                                   verbose_name='Турнир',
                                   related_name='competitors',
                                   on_delete=models.PROTECT)
    judoka = models.ForeignKey(Judoka,
                               verbose_name='Спортсмен',
                               related_name='tournaments',
                               on_delete=models.PROTECT)
    weight_class = models.ForeignKey(WeightClass,
                                     verbose_name='Весовая категория',
                                     # related_name='',
                                     on_delete=models.PROTECT)
    rating_points = models.IntegerField(default=0)
    slug = models.SlugField(verbose_name='Алиас', max_length=250)
    objects = models.Manager()

    class Meta:
        verbose_name = 'Участник турнира'
        verbose_name_plural = 'Участники турнира'
        # Уникальное сочитание полей
        unique_together = ('tournament', 'judoka')
        ordering = ('tournament', 'judoka')

    def get_absolute_url(self):
        return reverse('tournament:competitor',
                       args=[self.slug])

    def __str__(self):
        return self.judoka.short_name


class Tatami(models.Model):
    """
    Модель татами
    """
    tournament = models.ForeignKey(Tournament,
                                   verbose_name='Татами',
                                   related_name='tatamis',
                                   on_delete=models.PROTECT)
    number = models.IntegerField(default=1)
    slug = models.SlugField(verbose_name='Алиас', max_length=250)
    objects = models.Manager()

    class Meta:
        verbose_name = 'Татами'
        verbose_name_plural = 'Татами'
        unique_together = ('tournament', 'number')
        ordering = ('tournament', 'number')

    def get_absolute_url(self):
        return reverse('tournament:tatami',
                       args=[self.slug])

    def __str__(self):
        return ' '.join(['Татами', str(self.number)])


class TournamentTable(models.Model):
    """
    Модель турнирной таблицы с учетом весовой категории
    """
    COMPETITION_SYSTEM = (
        ('olympic', 'Олимпийская'),
        ('round', 'Круговая'),
        ('mixed', 'Смешанная'),
    )
    tournament = models.ForeignKey(Tournament,
                                   verbose_name='Турнир',
                                   related_name='tournament_tables',
                                   on_delete=models.PROTECT)
    weight_class = models.ForeignKey(WeightClass,
                                     verbose_name='Весовая категория',
                                     # related_name='',
                                     on_delete=models.PROTECT)
    competition_system = models.CharField(verbose_name='Система соревнований',
                                          max_length=7,
                                          choices=COMPETITION_SYSTEM,
                                          default='olympic')
    slug = models.SlugField(verbose_name='Алиас', max_length=250)
    objects = models.Manager()

    class Meta:
        verbose_name = 'Турнирная таблица'
        verbose_name_plural = 'Турнирные таблицы'
        unique_together = ('tournament', 'weight_class')
        ordering = ('tournament', 'weight_class')

    def get_absolute_url(self):
        return reverse('tournament:tournament_table',
                       args=[self.slug])

    def __str__(self):
        return ' -----> '.join([
            self.tournament.__str__(),
            self.weight_class.__str__()
        ])


class TournamentTableGroup(models.Model):
    """
    Модель групп турнирных таблиц (А и Б)
    """
    GROUP_CHOICES = (
        ('A', 'Группа А'),
        ('B', 'Группа Б')
    )
    tournament_table = models.ForeignKey(TournamentTable,
                                         verbose_name='Турнирная таблица',
                                         related_name='table_groups',
                                         on_delete=models.PROTECT)
    group = models.CharField(verbose_name='Турнирная группа',
                             max_length=1,
                             choices=GROUP_CHOICES,
                             default='A')
    slug = models.SlugField(verbose_name='Алиас', max_length=250)

    class Meta:
        verbose_name = 'Турнирная группа'
        verbose_name_plural = 'Турнирные группы'
        unique_together = ('tournament_table', 'group')

    def get_absolute_url(self):
        return reverse('tournament:tournament_table_group',
                       args=[self.slug])

#
#
#
#
# class TournamentWeightClass(models.Model):
#     """
#     Модель разделения турнира по весовым категориям
#     """
#     COMPETITION_SYSTEM = (
#         ('olympic', 'Олимпийская'),
#         ('round', 'Круговая'),
#         ('mixed', 'Смешанная'),
#     )
#     tournament = models.ForeignKey(Tournament,
#                                    verbose_name='Турнир',
#                                    related_name='weight_classes',
#                                    on_delete=models.PROTECT)
#     weight_class = models.ForeignKey(WeightClass,
#                                      verbose_name='Весовая категория',
#                                      # related_name='',
#                                      on_delete=models.PROTECT)
#     competition_system = models.CharField(verbose_name='Система соревнований',
#                                           max_length=7,
#                                           choices=COMPETITION_SYSTEM,
#                                           default='olympic')
#     slug = models.SlugField(verbose_name='Алиас', max_length=250)
#     objects = models.Manager()
#
#     class Meta:
#         verbose_name = 'Весовая категория турнира'
#         verbose_name_plural = 'Весовые категории турнира'
#         ordering = ('weight_class', )
#
#     def get_absolute_url(self):
#         return reverse('tournament:tournament_weight_class',
#                        args=[self.slug])
#
#
# class QueueWeightClass(models.Model):
#     """
#     Модель очереди выступления весовых категорий турнира
#     """
#     tournament_weight_class = models.ForeignKey(TournamentWeightClass,
#                                                 verbose_name='Соревнования для весовой категории',
#                                                 related_name='tournament_weight_classes',
#                                                 on_delete=models.PROTECT)
#     order = models.IntegerField(verbose_name='Очередность выступления')
#     slug = models.SlugField(verbose_name='Алиас', max_length=250)
#     objects = models.Manager()
#
#     class Meta:
#         verbose_name = 'Очередь выступления весовой группы'
#         verbose_name_plural = 'Очередь выступления весовых групп'
#         ordering = ('tournament_weight_class', 'order')
#
#     def get_absolute_url(self):
#         return reverse('tournament:queue_weight_class',
#                        args=[self.slug])
#
#
# # class TournamentTable(models.Model):
# #     """
# #     Модель турнирной таблицы для весовых категорий
# #     """
# #     tournament_weight_class = models.ForeignKey(TournamentWeightClass,
# #                                                 verbose_name='Весовая категория в турнире',
# #                                                 related_name='',
# #                                                 on_delete=models.PROTECT)
#
#
# class Fight(models.Model):
#     """
#     Модель поединка
#     """
#     GROUP_CHOICES = (
#         ('a', 'А'),
#         ('b', 'Б')
#     )
#     group = models.CharField(verbose_name='Группа',
#                              max_length=1,
#                              choices=GROUP_CHOICES,
#                              default='a')
#     fighter_0 = models.ForeignKey(Judoka,
#                                   verbose_name='Боец 0',
#                                   related_name='fighters0',
#                                   on_delete=models.PROTECT)
#     fighter_1 = models.ForeignKey(Judoka,
#                                   verbose_name='Боец 1',
#                                   related_name='fighters1',
#                                   on_delete=models.PROTECT)
#     winner = models.ForeignKey(Judoka,
#                                verbose_name='Победитель',
#                                related_name='winners',
#                                on_delete=models.PROTECT)
#
#     class Meta:
#         verbose_name = 'Поединок'
#         verbose_name_plural = 'Поединки'
#         ordering = ('group', )
#
#
# class TournamentTable(models.Model):
#     """
#     Модель турнирной таблицы
#     """
#     tournament_weight_class = models.ForeignKey(TournamentWeightClass,
#                                                 verbose_name='Весовая категория',
#                                                 related_name='tournament_tables',
#                                                 on_delete=models.PROTECT)
#     # fight =