from .models import Passage
import django_tables2 as dt2
from django.utils.translation import gettext as _


class PassageTable(dt2.Table):
    id = dt2.Column()
    person__name = dt2.Column(verbose_name=_('Person'))
    person__company = dt2.Column(verbose_name=_('Company'))
    person__area = dt2.Column(verbose_name=_('Area'))
    person__department = dt2.Column(verbose_name=_('Department'))
    app__name = dt2.Column(verbose_name=_('App'))
    start_time = dt2.DateTimeColumn(verbose_name=_('Start time'))
    item__item_type = dt2.Column(verbose_name=_('Item'))
    duration = dt2.Column(orderable=False, verbose_name=_('Duration'))

    class Meta:
        model = Passage
        template_name = 'django_tables2/bootstrap4.html'
        fields = ('id',
                  'person__name',
                  'person__company',
                  'person__area',
                  'person__department',
                  'app__name',
                  'start_time',
                  'item__item_type')
