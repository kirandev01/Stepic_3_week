# Generated by Django 3.1.1 on 2020-10-17 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_auto_20201017_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speciality',
            name='picture',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]