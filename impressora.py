#!/usr/bin/env python
# -*- coding: utf-8 -*-
from maquina import Maquina

class Impressora(Maquina):
    impressoras=[]
    def __init__(self, codigo_patrimonio, descricao ,velocidade):
        super(Impressora,self).__init__(codigo_patrimonio, descricao)
        self._validar_valor_positivo(velocidade)
        self._velocidade = velocidade
        self._host = None
        self._fila = []
        Impressora.armazenar(self)
          
    def alterar_velocidade(self,velocidade):
        self._validar_valor_positivo(velocidade)
        self._velocidade = velocidade
    
    def imprimir(self):
        if self._fila != []:
            impressao_atual = self._fila.pop(-1)
            print 30*'-', 'IMPRIMINDO',30*'-'
            print 'ARQUIVO:', impressao_atual.arquivo
            print 'USUARIO:', impressao_atual.usuario.nome
            for x in range(impressao_atual.copias):
                print 'Copia',  x+1
            impressao_atual.remover_impressao()
    
    def adicionar_impressao(self, impressao):
        self._fila.append(impressao)
             
    def remover_impressao_fila(self, impressao=None):
        if impressao == None and self._fila != []:
            self._fila.pop(-1).remover_impressao()
        elif impressao in self._fila:
            impressao.remover_impressao()
            self._fila.remove(impressao)
        else:
            raise ValueError    
        
    def adicionar_host(self,host):
        if self._host == None:
            self._host = host
        else:
            raise ValueError

#    def adicionar_host(self,host):
#        self._tem_host()
#        self._host = host
#        self._host._impressoras.append(self)

#    def _tem_host(self):
#        if self.host != None:
#            raise ValueError


    def remover_host(self):
        self._host = None     
            
    def obter_velocidade(self):
        return self._velocidade
    
    def obter_fila(self):
        return self._fila
    
    def obter_host(self):
        return self._host
   
    def remover_todas_fila_impressao(self):
        if self._fila != []:
            self._fila.pop(-1).remover_impressao()
            self.remover_todas_fila_impressao()
            
    def destruir_maquina(self):
        if self.host != None:
            self.host.remover_impressora(self)
        if self.fila != []:
            raise ValueError
        Impressora.destruir(self)
        Maquina.destruir(self) 
    
#EXIBIÇÃO - HELPERS
    def _truncate(self,string,tamanho=32):
        return string+((tamanho-len(string))*' ') if len(string) < tamanho else string[:tamanho-3]+'...'

    def linha_lista(self,impressora,impressao):
        a = '| ', impressora._truncate(impressao.arquivo),' | ', impressora._truncate(impressao.usuario.nome) , '|'
        a = ''.join(a)
        return a
    
    
    
    @classmethod
    def destruir(cls,impressora):
        Impressora.impressoras.remove(impressora)        
    @classmethod
    def armazenar(cls, impressora):
        Impressora.impressoras.append(impressora)

    @classmethod
    def mostrar_fila(cls):
        if Impressora.impressoras == []:
            return 'Nenhuma impressora'
        else:
            for impressora in Impressora.impressoras:
                space= 10*'-'
                print space,' ARQUIVOS EM FILA DA IMPRESSORA: ', impressora.descricao, space
                print '|',space, ' ARQUIVOS ',space,'|',space,' USUARIO ', space,'|'
                if impressora.fila!=[]:
                    for impressao in impressora.fila:
                        print impressora.linha_lista(impressora,impressao)



    velocidade = property(obter_velocidade, alterar_velocidade)
    host = property(obter_host)
    fila = property(obter_fila)
