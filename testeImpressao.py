#!/usr/bin/env python
# -*- coding: utf-8 -*-
  
import unittest
from should_dsl import should, should_not
from maquina import Maquina
from servidor import Servidor
from impressora import Impressora
from impressao import Impressao
from usuario import Usuario

class testeImpressao(unittest.TestCase):

    def test_obter_impressao(self):
        usuario = Usuario('mauro','123456')
        impressora = Impressora(20,'Printer',40)
        impressao = Impressao('arquivo1.txt',impressora, usuario,40)
       
        (impressao._validar_valor_positivo,1) |should_not| throw(ValueError)
        (impressao._validar_valor_positivo,0) |should| throw(ValueError)

        impressao.copias |should| equal_to(40)
        impressao.arquivo |should| equal_to('arquivo1.txt')
        impressao.usuario |should| equal_to(usuario)

        impressora.remover_impressao_fila()        
        usuario.apagar_usuario()
        impressora.destruir_maquina()
        
    def test_obter_mais_copias(self):
        usuario = Usuario('mauro','123456')
        impressora = Impressora(20,'Printer',40)
        impressao = Impressao('arquivo1.txt',impressora, usuario,10)
        impressao.copias |should| equal_to(10)
#        impressao2 = Impressao('arquivo1.txt',impressora, usuario)
#        impressao.copias |should| equal_to(11)
        
        impressora.remover_impressao_fila()        
        usuario.apagar_usuario()
        impressora.destruir_maquina()


          
if __name__ == "__main__":
    unittest.main()

