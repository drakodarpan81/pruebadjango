# Generated by Django 4.1.2 on 2023-02-08 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CatCoordinacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('nombre_coordinacion', models.CharField(max_length=50, unique=True, verbose_name='Nombre de la coordinación')),
                ('nombre_area', models.CharField(choices=[('3', 'Inovación y Gestión de Calidad'), ('2', 'Administración'), ('0', 'Vigilancia Sanitaria'), ('1', 'Vigilancia Epidemiologica')], max_length=1, verbose_name='Nombre del área')),
                ('estado', models.BooleanField(default=True, verbose_name='Activo / Inactivo')),
                ('fecha_alta', models.DateField(auto_now_add=True, verbose_name='Fecha alta')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha modificacion')),
            ],
            options={
                'verbose_name': 'CatCoordinacion',
                'verbose_name_plural': 'CatCoordinaciones',
            },
        ),
        migrations.CreateModel(
            name='CatPersonalEncargadoArea',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('nombre_empleado', models.CharField(max_length=100, unique=True, verbose_name='Nombre del empleado')),
            ],
            options={
                'verbose_name': 'CatPersonalEncargadoArea',
                'verbose_name_plural': 'CatPersonalEncargadoAreas',
            },
        ),
        migrations.CreateModel(
            name='CatPersonalLaboratorio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('nombre_empleado', models.CharField(max_length=100, unique=True, verbose_name='Nombre del empleado')),
                ('rfc', models.CharField(max_length=15, unique=True, verbose_name='RFC')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('fecha_ingreso', models.DateField(auto_now_add=True, verbose_name='Fecha ingreso')),
            ],
            options={
                'verbose_name': 'CatPersonalLaboratorio',
                'verbose_name_plural': 'CatPersonalLaboratorios',
            },
        ),
        migrations.CreateModel(
            name='HistoricalCatPersonalLaboratorio',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True, verbose_name='id')),
                ('nombre_empleado', models.CharField(db_index=True, max_length=100, verbose_name='Nombre del empleado')),
                ('rfc', models.CharField(db_index=True, max_length=15, verbose_name='RFC')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('fecha_ingreso', models.DateField(blank=True, editable=False, verbose_name='Fecha ingreso')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical CatPersonalLaboratorio',
                'verbose_name_plural': 'historical CatPersonalLaboratorios',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCatPersonalEncargadoArea',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True, verbose_name='id')),
                ('nombre_empleado', models.CharField(db_index=True, max_length=100, verbose_name='Nombre del empleado')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical CatPersonalEncargadoArea',
                'verbose_name_plural': 'historical CatPersonalEncargadoAreas',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCatCoordinacion',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True, verbose_name='id')),
                ('nombre_coordinacion', models.CharField(db_index=True, max_length=50, verbose_name='Nombre de la coordinación')),
                ('nombre_area', models.CharField(choices=[('3', 'Inovación y Gestión de Calidad'), ('2', 'Administración'), ('0', 'Vigilancia Sanitaria'), ('1', 'Vigilancia Epidemiologica')], max_length=1, verbose_name='Nombre del área')),
                ('estado', models.BooleanField(default=True, verbose_name='Activo / Inactivo')),
                ('fecha_alta', models.DateField(blank=True, editable=False, verbose_name='Fecha alta')),
                ('fecha_modificacion', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha modificacion')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('coordinador_responsable', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='personal.catpersonallaboratorio')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('responsable_area', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='personal.catpersonalencargadoarea')),
            ],
            options={
                'verbose_name': 'historical CatCoordinacion',
                'verbose_name_plural': 'historical CatCoordinaciones',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddField(
            model_name='catpersonalencargadoarea',
            name='nombre_empleado_coordinador',
            field=models.ManyToManyField(through='personal.CatCoordinacion', to='personal.catpersonallaboratorio'),
        ),
        migrations.AddField(
            model_name='catcoordinacion',
            name='coordinador_responsable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CatPersonalLaboratorio', to='personal.catpersonallaboratorio'),
        ),
        migrations.AddField(
            model_name='catcoordinacion',
            name='responsable_area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CatPersonalLaboratorio', to='personal.catpersonalencargadoarea'),
        ),
    ]