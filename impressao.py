#!/usr/bin/env python
# -*- coding: utf-8 -*-
from impressora import Impressora
from usuario import Usuario
class Impressao(object):
    impressoes = []
    def __init__(self, arquivo,impressora,usuario,copias=1):
        self._validar_impressao(arquivo,impressora,usuario,copias)
        self._arquivo = arquivo
        self._impressora = impressora
        self._usuario = usuario
        self._copias = copias
        self._impressora.adicionar_impressao(self)
        Impressao.armazenar(self)

    def obter_arquivo(self):
        return self._arquivo

    def obter_usuario(self):
        return self._usuario
    
    def obter_copias(self):
        return self._copias
   
    def alterar_copias(self,copias):
        self._copias=copias
        
    def obter_impressora(self):
        return self._impressora
   
    def remover_impressao(self):
        Impressao.destruir(self)
               
    def _validar_impressao(self,arquivo,impressora,usuario,copias):
        self._validar_valor_positivo(copias)
        self._validar_impressora(impressora)
        self._validar_usuario(usuario)
        self._verificar_nova(usuario,arquivo,copias)
            
    def _validar_usuario(self,usuario):
        if not isinstance(usuario, Usuario):
            raise ValueError
        elif usuario.atual_estacao == None:
            raise ValueError    
   
    def _validar_impressora(self,impressora):
        if not isinstance(impressora, Impressora):
            raise ValueError
        elif impressora.host == None:
            raise ValueError    
                   
                    
    def _validar_valor_positivo(self, valor):
        if valor <= 0:
            raise ValueError
                
    def _verificar_nova(self, usuario, arquivo,copias):
        for impressao in  Impressao.impressoes:
            if impressao.usuario == usuario and impressao.arquivo == arquivo:
                impressao.copias+=copias
                raise ValueError


                
    @classmethod
    def destruir(cls,impressao):
        Impressao.impressoes.remove(impressao)        
    @classmethod
    def armazenar(cls, impressao):
        Impressao.impressoes.append(impressao)


    impressora = property(obter_impressora)
    arquivo = property(obter_arquivo)
    usuario = property(obter_usuario)
    copias = property(obter_copias,alterar_copias)
