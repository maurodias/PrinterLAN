#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Maquina(object):
    maquinas=[]
    def __init__(self, codigo_patrimonio, descricao ):
        self._verificar_identidade(codigo_patrimonio)
        self._codigo_patrimonio = codigo_patrimonio
        self._descricao = descricao
        Maquina.armazenar(self)

    def alterar_codigo(self,codigo_patrimonio):
        self._verificar_identidade(codigo_patrimonio)
        self._codigo_patrimonio = codigo_patrimonio
    
    def alterar_descricao(self,descricao):
        self._descricao = descricao

    def obter_codigo(self):
        return self._codigo_patrimonio
    
    def obter_descricao(self):
        return self._descricao
        
    def _verificar_identidade(self, cod):
        for maquina in Maquina.maquinas:
            if cod == maquina.codigo:
                print maquina.descricao , type(maquina) , 'ja existe o codigo', cod
                
                raise ValueError
    
    def _validar_valor_positivo(self, valor):
        if valor <= 0:
            raise ValueError
            
    def verificar_se_estacao(self):
        if isinstance(self, Estacao):
            return True
        else:
            return False
            
    def destruir_maquina(self):
        Maquina.destruir(self)
        
    @classmethod
    def armazenar(cls, maquina):
        Maquina.maquinas.append(maquina)
        
    @classmethod        
    def destruir(cls, maquina):
        Maquina.maquinas.remove(maquina)

    descricao = property(obter_descricao, alterar_descricao)
    codigo = property(obter_codigo, alterar_codigo)
