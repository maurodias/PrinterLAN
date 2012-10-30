#!/usr/bin/env python
# -*- coding: utf-8 -*-
from estacao import Estacao

class Usuario(object):
    usuarios=[]
    def __init__(self, nome, senha):
        self._verificar_identidade(nome)
        self._nome = nome
        self._senha = senha
        self._atual_estacao = None
        Usuario.armazenar(self)
    
    def logar(self,estacao):
        self._verificar_se_estacao(estacao)
        self._verificar_disponibilidade()
        estacao.logar(self)
        self._atual_estacao = estacao
       
    def deslogar(self):
        if self.atual_estacao != None:
            self._atual_estacao.deslogar()
            self._atual_estacao == None
           
    def alterar_nome(self,nome):
        self._verificar_identidade(nome)
        self._nome = nome
    
    def alterar_senha(self,senha):
        self._senha = senha

    def obter_nome(self):
        return self._nome
    
    def obter_senha(self):
        return self._senha
        
    def obter_atual_estacao(self):
        return self._atual_estacao
        
    def apagar_usuario(self):
        self.deslogar()
        Usuario.apagar(self)
    
    def listar_impressoes(self):
        space= 5*'-'
        print 6*space,' ARQUIVOS EM FILA DO USUARIO: ', self, 6*space
        print '|',space, ' ARQUIVOS ',space,'|',space,' ESTACAO ', space
        for impressao in Impressao.impressoes:
            if self == impressao.usuario:
                print '| ', self._truncate(impressao.arquivo), ' | ', impressao.estacao.codigo,': ', self._truncate(impressao.estacao.descricao, 15) 
                    
    def _truncate(self,string,tamanho=35):
        return string if len(string) < tamanho else string[:tamanho-3]+'...'

    def _verificar_disponibilidade(self):
        if self.atual_estacao != None:
            raise ValueError
    
    def _verificar_se_estacao(self,estacao):
        if not isinstance(estacao, Estacao):
            raise ValueError    
    
    def _verificar_identidade(self, nome):
        for usuario in Usuario.usuarios:
            if nome == usuario.nome:
                raise ValueError
    
    @classmethod
    def armazenar(cls, usuario):
        Usuario.usuarios.append(usuario)
        
    @classmethod        
    def apagar(cls, usuario):
        Usuario.usuarios.remove(usuario)

    nome = property(obter_nome, alterar_nome)
    senha = property(obter_senha, alterar_senha)
    atual_estacao = property(obter_atual_estacao)
