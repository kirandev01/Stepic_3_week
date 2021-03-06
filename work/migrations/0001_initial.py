# Generated by Django 3.1.1 on 2020-10-17 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=50)),
                ('employee_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('skils', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('salary_min', models.IntegerField()),
                ('salary_max', models.IntegerField()),
                ('published_at', models.DateField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='work.company')),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='work.speciality')),
            ],
        ),
    ]
