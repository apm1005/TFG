# Generated by Django 2.2.6 on 2019-11-21 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('environments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('server', models.ForeignKey(blank=True, db_column='server', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='environments.Environment')),
            ],
        ),
    ]
