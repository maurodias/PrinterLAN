#!/usr/bin/env python
# -*- coding: utf-8 -*-
  
import unittest
from should_dsl import should, should_not
from maquina import Maquina
from computador import Computador
from servidor import Servidor

class testeServidor(unittest.TestCase):

    def test_obter_servidor(self):
        servidor = Servidor(1,'PC',512,4088,128,10000)
        servidor.tamanho_max_buffer |should| equal_to(128)
        servidor.quantidade_max_buffer |should| equal_to(10000)
        servidor.impressoras |should| equal_to([])
        servidor.destruir_maquina()

    def test_alterar_servidor(self):
        servidor = Servidor(1,'PC',512,4088,128,10000)
        servidor.tamanho_max_buffer = 64
        servidor.tamanho_max_buffer |should| equal_to(64)
        servidor.quantidade_max_buffer = 2000
        servidor.quantidade_max_buffer |should| equal_to(2000)
        servidor.destruir_maquina()       
    
    def test_adicionar_impressoras(self):
        servidor = Servidor(1,'PC',512,4088,128,10000)
        servidor.adicionar_impressora("impressora")
        servidor.impressoras |should| equal_to(["impressora"])
        servidor.adicionar_impressora("impressora2")
        servidor.adicionar_impressora("impressora3")
        servidor.impressoras |should| equal_to(["impressora","impressora2","impressora3"])
        servidor.adicionar_impressora("impressora4")
#        should raise error, implemetar
        servidor.impressoras |should| equal_to(["impressora","impressora2","impressora3"])
        servidor.destruir_maquina()
    
    def test_remover_impressoras(self):
        servidor = Servidor(1,'PC',512,4088,128,10000)
        servidor.adicionar_impressora("impressora")
        servidor.remover_impressora("impressora")
        servidor.impressoras |should| equal_to([])
#        servidor.remover_impressora()
#        should raise error, implemetar
        servidor.destruir_maquina() 
         
if __name__ == "__main__":
    unittest.main()

