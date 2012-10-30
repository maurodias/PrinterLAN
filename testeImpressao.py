#!/usr/bin/env python
# -*- coding: utf-8 -*-
  
import unittest
from should_dsl import should, should_not
from maquina import Maquina
from servidor import Servidor
from impressora import Impressora
from impressao import Impressao
from usuario import Usuario
from estacao import Estacao

class testeImpressao(unittest.TestCase):

    def test_obter_impressao(self):
        estacao = Estacao(1,'DELL',4,512,'lab-8')
        servidor = Servidor(2,'PC',512,4088,128,10000)
        impressora = Impressora(20,'lASERjET HP',40)
        usuario = Usuario('mauro','123456')
        
        usuario.logar(estacao)
        servidor.adicionar_impressora(impressora)
        
        impressao = Impressao('arquivo1.txt',impressora, usuario)
       
        (impressao._validar_valor_positivo,1) |should_not| throw(ValueError)
        (impressao._validar_valor_positivo,0) |should| throw(ValueError)

        impressao.copias |should| equal_to(1)
        impressao.arquivo |should| equal_to('arquivo1.txt')
        impressao.usuario |should| equal_to(usuario)

        impressora.imprimir()
        usuario.apagar_usuario()
        impressora.destruir_maquina()      
        estacao.destruir_maquina()        
        servidor.destruir_maquina()
        
    def test_obter_mais_copias(self):
        estacao = Estacao(1,'DELL',4,512,'lab-8')
        servidor = Servidor(2,'PC',512,4088,128,10000)
        impressora = Impressora(20,'lASERjET HP',40)
        usuario = Usuario('mauro','123456')
        
        usuario.logar(estacao)
        servidor.adicionar_impressora(impressora)
        
        impressao = Impressao('arquivo1.txt',impressora, usuario)
       
        (impressao._validar_valor_positivo,1) |should_not| throw(ValueError)
        (impressao._validar_valor_positivo,0) |should| throw(ValueError)

        impressao.copias |should| equal_to(1)
        impressao.arquivo |should| equal_to('arquivo1.txt')
        impressao.usuario |should| equal_to(usuario)

        impressora.imprimir()
        usuario.apagar_usuario()
        impressora.destruir_maquina()      
        estacao.destruir_maquina()        
        servidor.destruir_maquina()


          
if __name__ == "__main__":
    unittest.main()

