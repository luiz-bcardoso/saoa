# Generated by Django 4.2.14 on 2024-08-23 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0002_alter_avaliacao_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='merito_relevancia_responsavel',
            field=models.CharField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], max_length=1, null=True, verbose_name='Relevância: O artigo aborda um problema atual e/ou relevante na área em que foi submetido ao evento?'),
        ),
    ]
