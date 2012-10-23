#!/usr/bin/env python
# -*- coding: utf-8 -*-
from maquina import Maquina
from servidor import Servidor

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
            if self._validar_host(host):
                self._host = host
                self._host._impressoras.append(self)
        else:
            return "Remova a conexão com atual servidor"

    def remover_host(self):
        if self._host != None:
            self._host._impressoras.remove(self)
            self._host = None        
            
    def obter_velocidade(self):
        return self._velocidade
    
    def obter_host(self):
        return self._host
   
    def _validar_host(self,host):
        if isinstance(host, Servidor):
            if host.verificar_disponibilidade():
                return True
        return False
            
    def destruir_maquina(self):
        self.remover_host()
        Maquina.destruir(self)        

    velocidade = property(obter_velocidade, alterar_velocidade)
    host = property(obter_host)
