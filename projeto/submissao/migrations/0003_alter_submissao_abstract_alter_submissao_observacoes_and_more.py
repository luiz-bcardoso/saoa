# Generated by Django 4.2.14 on 2024-07-26 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissao', '0002_alter_submissao_arquivo_comite_etica_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissao',
            name='abstract',
            field=models.TextField(help_text='Máximo de 2000 caracteres. Se for colar texto de outro aplicativo, certifique-se que o título esteja completo', max_length=2000, verbose_name='Abstract *'),
        ),
        migrations.AlterField(
            model_name='submissao',
            name='observacoes',
            field=models.TextField(blank=True, help_text='Máximo de 1000 caracteres', max_length=1000, null=True, verbose_name='Registre justificativas e/ou apontamentos para o responsável da submissão'),
        ),
        migrations.AlterField(
            model_name='submissao',
            name='palavras_chave',
            field=models.CharField(help_text='Escreva as palavras-chave separadas por ponto-e-vígura. Exemplo: Redes Neurais; Aprendizado de Máquina; Descoberta de Conhecimento', max_length=150, verbose_name='Palavras-chave *'),
        ),
        migrations.AlterField(
            model_name='submissao',
            name='resumo',
            field=models.TextField(help_text='Máximo de 2000 caracteres. Se for colar texto de outro aplicativo, certifique-se que o título esteja completo', max_length=2000, verbose_name='Resumo *'),
        ),
        migrations.AlterField(
            model_name='submissao',
            name='titulo',
            field=models.CharField(help_text='Máximo de 250 caracteres. Se for colar texto de outro aplicativo, certifique-se que o título esteja completo', max_length=250, verbose_name='Título *'),
        ),
    ]
