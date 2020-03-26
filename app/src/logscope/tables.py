from .models import Passage
import django_tables2 as dt2


class PassageTable(dt2.Table):
    id = dt2.Column()
    person__name = dt2.Column()
    person__company = dt2.Column()
    person__area = dt2.Column()
    person__department = dt2.Column()
    app__name = dt2.Column()
    start_time = dt2.DateTimeColumn()
    item__item_type = dt2.Column()
    duration = dt2.Column(orderable=False)

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
