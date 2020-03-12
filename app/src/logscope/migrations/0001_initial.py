# Generated by Django 2.2.6 on 2020-03-12 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=40)),
                ('ip_address', models.CharField(blank=True, max_length=17, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('instant', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Eventtype',
            fields=[
                ('type', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=70, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ip_address', models.CharField(blank=True, max_length=17, null=True)),
                ('mac_address', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Itemtype',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=30)),
                ('brand', models.CharField(blank=True, max_length=30)),
                ('model', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Passage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('login', models.CharField(blank=True, max_length=20)),
                ('company', models.CharField(blank=True, max_length=50)),
                ('division', models.CharField(blank=True, max_length=50)),
                ('area', models.CharField(blank=True, max_length=50)),
                ('department', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.AddConstraint(
            model_name='person',
            constraint=models.UniqueConstraint(fields=('login',), name='unique user login'),
        ),
        migrations.AddField(
            model_name='passage',
            name='app',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='logscope.App'),
        ),
        migrations.AddField(
            model_name='passage',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='logscope.Event'),
        ),
        migrations.AddField(
            model_name='passage',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='logscope.Item'),
        ),
        migrations.AddField(
            model_name='passage',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='logscope.Person'),
        ),
        migrations.AddField(
            model_name='item',
            name='item_type',
            field=models.ForeignKey(blank=True, db_column='item_type', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='logscope.Itemtype'),
        ),
        migrations.AddField(
            model_name='item',
            name='persons',
            field=models.ManyToManyField(to='logscope.Person'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(blank=True, db_column='event_type', on_delete=django.db.models.deletion.DO_NOTHING, to='logscope.Eventtype'),
        ),
        migrations.AddField(
            model_name='app',
            name='server',
            field=models.ForeignKey(blank=True, db_column='server', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='logscope.Environment'),
        ),
        migrations.AddConstraint(
            model_name='item',
            constraint=models.UniqueConstraint(fields=('mac_address',), name='unique mac address'),
        ),
    ]
