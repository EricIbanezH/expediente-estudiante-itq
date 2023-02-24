# Generated by Django 4.1.7 on 2023-02-23 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=100)),
                ('no_control', models.CharField(max_length=8)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descr', models.CharField(max_length=100)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=100)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Entrega_Doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=100)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.alumnos')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rol', models.CharField(max_length=20)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tipo_Archivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extension', models.CharField(max_length=5)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tipo_Tramite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('tiempo_estimado', models.IntegerField(default=5)),
                ('habilitado', models.BooleanField()),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tramite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.alumnos')),
                ('tramite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.tipo_tramite')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tipo_Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('tamano_MB', models.IntegerField(default=4)),
                ('tipo_arch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.tipo_archivo')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Rel_Tram_Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.rol')),
                ('tramite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.tipo_tramite')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Rel_Tram_Doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.tipo_documento')),
                ('tramite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.tipo_tramite')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Observ_Tramite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('comentario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.comentarios')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.estado')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.empleados')),
                ('tramite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.tramite')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Observ_Doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('comentario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.comentarios')),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.entrega_doc')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.estado')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.empleados')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='entrega_doc',
            name='tipo_doc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.tipo_documento'),
        ),
        migrations.AddField(
            model_name='empleados',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.rol'),
        ),
    ]
