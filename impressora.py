#!/usr/bin/env python
# -*- coding: utf-8 -*-
from maquina import Maquina

class Impressora(Maquina):
    def __init__(self, codigo_patrimonio, descricao ,velocidade,host):
        super(Impressora,self).__init__(codigo_patrimonio, descricao)
        self._validar_valor_positivo(velocidade)
        self._velocidade = velocidade
#        self._validar_host(host)
        self._host = host
  
    def alterar_velocidade(self,velocidade):
        self._validar_valor_positivo(velocidade)
        self._velocidade = velocidade
    
    def alterar_host(self,host):
#        self._validar_host(host)
        self._host = host

    def obter_velocidade(self):
        return self._velocidade
    
    def obter_host(self):
        return self._host
        
    velocidade = property(obter_velocidade, alterar_velocidade)
    host = property(obter_host, alterar_host)
