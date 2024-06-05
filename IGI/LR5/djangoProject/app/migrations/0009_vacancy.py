# Generated by Django 4.2.11 on 2024-05-12 12:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(help_text='Unique ID', primary_key=True, serialize=False)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now, help_text='Creation date')),
                ('lastUpdate', models.DateTimeField(default=django.utils.timezone.now, help_text='Update date')),
                ('position', models.CharField(help_text='The name of the position', max_length=100)),
                ('description', models.TextField(help_text='The description of the job')),
                ('salary', models.IntegerField(help_text='Monthly salary (gross)')),
            ],
            options={
                'db_table': 'vacancies',
                'ordering': ['salary'],
            },
        ),
    ]
