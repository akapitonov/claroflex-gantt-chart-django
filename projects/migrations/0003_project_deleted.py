# Generated by Django 3.1.5 on 2021-03-15 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20210315_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Deleted?'),
        ),
    ]
