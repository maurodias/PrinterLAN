#!/usr/bin/env python
# -*- coding: utf-8 -*-
from maquina import Maquina
from computador import Computador
from impressora import Impressora

class Servidor(Computador):
 
    def __init__(self, codigo_patrimonio, descricao ,hd,memoria,tamanho_max_buffer,quantidade_max_buffer):
        super(Servidor,self).__init__(codigo_patrimonio, descricao ,hd,memoria)
        self._validar_valor(quantidade_max_buffer)
        self._quantidade_max_buffer = quantidade_max_buffer
        self._validar_valor(tamanho_max_buffer)
        self._tamanho_max_buffer = tamanho_max_buffer
        self._impressoras=[]
        #cada servidor pode ter até 3 impressoras
        
    def alterar_quantidade_max_buffer(self,quantidade_max_buffer):
        self._validar_valor(quantidade_max_buffer)
        self._quantidade_max_buffer = quantidade_max_buffer
    
    def alterar_tamanho_max_buffer(self,tamanho_max_buffer):
        self._validar_valor(tamanho_max_buffer)
        self._tamanho_max_buffer = tamanho_max_buffer

    def obter_quantidade_max_buffer(self):
        return self._quantidade_max_buffer
    
    def obter_tamanho_max_buffer(self):
        return self._tamanho_max_buffer
        
    def obter_impressoras(self):
        return self._impressoras
        
    def adicionar_impressora(self, impressora):
        self._verificar_disponibilidade()
        self._validar_se_impressora(impressora)
        impressora.adicionar_host(self)
        self.impressoras.append(impressora)
    
    def remover_impressora(self, impressora):
        if impressora in self.impressoras:
            impressora.remover_host()
            self.impressoras.remove(impressora)
        else:
            raise ValueError
    
    def _verificar_disponibilidade(self):
        if len(self._impressoras) >= 3 :
            raise ValueError
            
    def _validar_se_impressora(self,impressora):
        if not isinstance(impressora, Impressora):
            raise ValueError

    def desconectar_todas_impressoras(self):
        for impressora in self._impressoras:
            impressora.remover_host() 
        self._impressoras=[]   
    
    def destruir_maquina(self):
        if len(self._impressoras) > 0:
            raise ValueError
        Maquina.destruir(self)        

    impressoras = property(obter_impressoras)
    tamanho_max_buffer = property(obter_tamanho_max_buffer, alterar_tamanho_max_buffer)
    quantidade_max_buffer = property(obter_quantidade_max_buffer, alterar_quantidade_max_buffer)
