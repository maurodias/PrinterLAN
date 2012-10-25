#!/usr/bin/env python
# -*- coding: utf-8 -*-
from maquina import Maquina

class Impressora(Maquina):
    def __init__(self, codigo_patrimonio, descricao ,velocidade):
        super(Impressora,self).__init__(codigo_patrimonio, descricao)
        self._validar_valor_positivo(velocidade)
        self._velocidade = velocidade
        self._host = None
  
    def alterar_velocidade(self,velocidade):
        self._validar_valor_positivo(velocidade)
        self._velocidade = velocidade
    
    def adicionar_host(self,host):
        if self._host == None:
            self._host = host
        else:
            raise ValueError

#    def adicionar_host(self,host):
#        self._tem_host == None
#        self._host = host
#        self._host._impressoras.append(self)

#    def _tem_host(self):
#        if self.host != None:
#            raise ValueError


    def remover_host(self):
        self._host = None     
            
    def obter_velocidade(self):
        return self._velocidade
    
    def obter_host(self):
        return self._host
   
    def destruir_maquina(self):
        if self.host != None:
            self.host.remover_impressora(self)
        Maquina.destruir(self)        

    velocidade = property(obter_velocidade, alterar_velocidade)
    host = property(obter_host)
