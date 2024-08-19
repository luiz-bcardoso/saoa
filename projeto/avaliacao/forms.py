from django import forms
from django.db import models

from evento.models import Evento
from usuario.models import Usuario 

from .models import Avaliacao


class AvaliacaoForm(forms.ModelForm):
    avaliador_responsavel = forms.ModelChoiceField(label='Selecione um membro como avaliador 1 *', queryset=Usuario.usuarios_ativos.all(), required=True)
    avaliador_suplente = forms.ModelChoiceField(label='Selecione um membro como avaliador 2 *', queryset=Usuario.usuarios_ativos.all(), required=True)
    avaliador_convidado = forms.ModelChoiceField(label='Selecione um membro como avaliador 3', queryset=Usuario.usuarios_ativos.all(), required=False)

    
    class Meta:
        model = Avaliacao
        fields = ['submissao', 'avaliador_responsavel', 'avaliador_suplente', 'avaliador_convidado', 'apto', 'rebanca', 'parecer_liberado', 
                  'parecer_avaliador_orientador', 'parecer_avaliador_responsavel', 'parecer_avaliador_suplente', 'parecer_avaliador_convidado',
                  'parecer_rebanca_avaliador_orientador', 'parecer_reavaliacao_avaliador_responsavel', 'parecer_reavaliacao_avaliador_suplente', 'parecer_reavaliacao_avaliador_convidado',
                    'merito_acompanhamento_orientador', 'merito_desenvolvimento_orientador', 'merito_redacao_orientador', 'merito_apresentacao_orientador', 
                    'merito_desenvolvimento_responsavel', 'merito_redacao_responsavel', 'merito_apresentacao_responsavel', 
                    'merito_desenvolvimento_suplente', 'merito_redacao_suplente', 'merito_apresentacao_suplente', 
                    'merito_desenvolvimento_convidado', 'merito_redacao_convidado', 'merito_apresentacao_convidado', 
                    'intercorrencias',
                    'nota_final_orientador', 'nota_final_responsavel', 'nota_final_suplente', 'nota_final_convidado', 
                    'media_final_avaliacao', 
                    'arquivo_corrigido_orientador', 'arquivo_corrigido_responsavel', 'arquivo_corrigido_suplente', 'arquivo_corrigido_convidado']
            
    def clean_avaliador_suplente(self):
        avaliador_responsavel = self.cleaned_data.get('avaliador_responsavel')
        avaliador_suplente = self.cleaned_data.get('avaliador_suplente')
        submissao = self.cleaned_data.get('submissao')

        if avaliador_responsavel:
            if (avaliador_suplente == avaliador_responsavel):
                raise forms.ValidationError('Um membro não pode ser ao mesmo tempo avaliador responsável e avaliador suplente')

            if (avaliador_suplente == submissao.orientador):
                raise forms.ValidationError('Um membro não pode ser ao mesmo tempo avaliador e orientador')

        return avaliador_suplente

    def clean_avaliador_responsavel(self):
        avaliador_responsavel = self.cleaned_data.get('avaliador_responsavel')        
        submissao = self.cleaned_data.get('submissao')
        
        if (avaliador_responsavel == submissao.orientador):
            raise forms.ValidationError('Um membro não pode ser ao mesmo tempo avaliador e orientador')

        return avaliador_responsavel


class BuscaAvaliacaoForm(forms.Form):
    nome_responsavel = forms.CharField(label='Nome do autor responsável', required=False)
    evento = forms.ModelChoiceField(label='Evento', queryset=Evento.objects.all(), required=False)
    nome_avaliador = forms.CharField(label='Nome do avaliador', required=False)