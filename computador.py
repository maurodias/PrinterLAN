#!/usr/bin/env python
# -*- coding: utf-8 -*-
from maquina import Maquina

class Computador(Maquina):
    def __init__(self, codigo_patrimonio, descricao ,hd,memoria):
        self._validar_valor(hd)
        self._hd = hd
        self._validar_valor(memoria)
        self._memoria = memoria
        super(Computador,self).__init__(codigo_patrimonio, descricao)
          
    def alterar_hd(self,hd):
        self._validar_valor(hd)
        self._hd = hd
    
    def alterar_memoria(self,memoria):
        self._validar_valor(memoria)
        self._memoria = memoria

    def obter_hd(self):
        return self._hd
    
    def obter_memoria(self):
        return self._memoria
        
    def _validar_valor(self, valor):
        if valor < 0:
            raise ValueError

    hd = property(obter_hd, alterar_hd)
    memoria = property(obter_memoria, alterar_memoria)
