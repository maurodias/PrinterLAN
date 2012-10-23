#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Usuario(object):
    usuarios=[]
    def __init__(self, nome, senha):
        self._verificar_identidade(nome)
        self._nome = nome
        self._senha = senha
        Usuario.armazenar(self)
    
    def alterar_nome(self,nome):
        self._verificar_identidade(nome)
        self._nome = nome
    
    def alterar_senha(self,senha):
        self._senha = senha

    def obter_nome(self):
        return self._nome
    
    def obter_senha(self):
        return self._senha
        
    def _verificar_identidade(self, nome):
        for usuario in Usuario.usuarios:
            if nome == usuario.obter_nome():
                raise ValueError
    
    def _validar_valor_positivo(self, valor):
        if valor <= 0:
            raise ValueError
            
    def apagar_usuario(self):
        Usuario.apagar(self)
        
    @classmethod
    def armazenar(cls, usuario):
        Usuario.usuarios.append(usuario)
        
    @classmethod        
    def apagar(cls, usuario):
        Usuario.usuarios.remove(usuario)

    nome = property(obter_nome, alterar_nome)
    senha = property(obter_senha, alterar_senha)
