#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from maquina import Maquina
from computador import Computador

class Estacao(Computador):
 
    def __init__(self, codigo_patrimonio, descricao ,hd,memoria,localizacao):
        self._localizacao = localizacao
        self._usuario='Livre'
        self._datahora=None
        super(Estacao,self).__init__(codigo_patrimonio, descricao,hd,memoria)
        
    def alterar_localizacao(self,localizacao):
        self._localizacao = localizacao

    def obter_localizacao(self):
        return self._localizacao
    
    def obter_usuario(self):
        return self._usuario
        
    def obter_datahora(self):
        return self._datahora
        
    def logar(self,usuario):
        self._verificar_disponibilidade()
        self._usuario = usuario
        self._datahora = datetime.now().strftime("%d/%m/%Y %H:%M")
    
    def deslogar(self):
            self._usuario = "Livre"
            self._datahora=None
    
    def _verificar_disponibilidade(self):
        if self._usuario != 'Livre':
            print 'tem usuario'
            raise ValueError
            
    @classmethod
    def listar_estacoes(self):
        print '-------', ' COD','    ------    ', 'USUÁRIO', ' ----------------------- ', 'DARA/HORA LOGIN', '-------'
        for maquina in Maquina.maquinas:
            if maquina.verificar_se_estacao():
                print '------- ', maquina.codigo,' ------    ', maquina.usuario, ' ----------------------- ' , maquina.datahora, ' -------\n'
                maquina.usuario.listar_impressoes()
                
    def destruir_maquina(self):
        self._verificar_disponibilidade()
        Maquina.destruir(self)        

    datahora = property(obter_datahora)
    usuario = property(obter_usuario)
    localizacao = property(obter_localizacao, alterar_localizacao)
