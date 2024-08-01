# Generated by Django 4.2.14 on 2024-08-01 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0002_evento_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='site',
            field=models.URLField(blank=True, help_text='Informe o site oficial do evento', max_length=100, null=True, verbose_name='Site do evento'),
        ),
    ]
