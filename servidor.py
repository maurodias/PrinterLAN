#!/usr/bin/env python
# -*- coding: utf-8 -*-
from maquina import Maquina
from computador import Computador

class Servidor(Computador):
    def __init__(self, codigo_patrimonio, descricao ,hd,memoria,tamanho_max_buffer,quantidade_max_buffer):
        super(Servidor,self).__init__(codigo_patrimonio, descricao ,hd,memoria)
        self._validar_valor(quantidade_max_buffer)
        self._quantidade_max_buffer = quantidade_max_buffer
        self._validar_valor(tamanho_max_buffer)
        self._tamanho_max_buffer = tamanho_max_buffer
        self._impressoras=[]
        
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
        if len(self.impressoras) < 3:
#            self._validar_impressora(impressora)
            self.impressoras.append(impressora)
    
    def remover_impressora(self, impressora):
        if impressora in self.impressoras:
            self.impressoras.remove(impressora)
    
    
    impressoras = property(obter_impressoras)
    tamanho_max_buffer = property(obter_tamanho_max_buffer, alterar_tamanho_max_buffer)
    quantidade_max_buffer = property(obter_quantidade_max_buffer, alterar_quantidade_max_buffer)
