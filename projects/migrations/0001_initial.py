# Generated by Django 3.1.5 on 2021-03-13 19:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Project name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Project Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('completed_at', models.DateTimeField(blank=True, null=True, verbose_name='Completed at')),
                ('responsible_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='responsible_user_projects', to=settings.AUTH_USER_MODEL, verbose_name='Responsible User')),
                ('user_created', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_created_projects', to=settings.AUTH_USER_MODEL, verbose_name='User created')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Task Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('start_date', models.DateField(verbose_name='Start date')),
                ('close_date', models.DateField(verbose_name='Close date')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='projects.project')),
                ('related_task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.projecttask')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Task user')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='project_files/%Y/%m/%d', verbose_name='Project file')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='projects.project')),
            ],
        ),
    ]