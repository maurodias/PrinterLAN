#!/usr/bin/env python
# -*- coding: utf-8 -*-
  
import unittest
from should_dsl import should, should_not
from maquina import Maquina
from computador import Computador
from servidor import Servidor
from impressora import Impressora

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
        impressora = Impressora(21,'Printer',40)
        impressora2 = Impressora(22,'Printer2',40)
        impressora3 = Impressora(23,'Printer3',50)
        impressora4 = Impressora(24,'Printer4',45)
        servidor = Servidor(1,'PC',512,4088,128,10000)
        
        servidor.adicionar_impressora(impressora)
        impressora.host |should| equal_to(servidor)
        servidor.impressoras |should| equal_to([impressora])
        
        servidor.adicionar_impressora(impressora2)
        servidor.adicionar_impressora(impressora3)
        servidor.impressoras |should| equal_to([impressora,impressora2,impressora3])

        (servidor._validar_se_impressora,impressora4) |should_not| throw(ValueError)
        (servidor._verificar_disponibilidade) |should| throw(ValueError)
       
        (servidor.destruir_maquina) |should| throw(ValueError) 
        servidor.desconectar_todas_impressoras()
        (servidor.destruir_maquina) |should_not| throw(ValueError)
        
        impressora2.destruir_maquina()
        impressora3.destruir_maquina()        
        impressora.destruir_maquina()
        impressora4.destruir_maquina()
        
        
    def test_remover_impressoras(self):
        servidor = Servidor(1,'PC',512,4088,128,10000)
        impressora = Impressora(21,'Printer',40)
        servidor.adicionar_impressora(impressora)

        (servidor.remover_impressora,"impressora") |should| throw(ValueError)
        (servidor.remover_impressora,impressora) |should_not| throw(ValueError)
        servidor.impressoras |should| equal_to([])
        
        impressora.destruir_maquina()
        servidor.destruir_maquina() 
        
        
    def test_destruir_impressora(self):
        servidor = Servidor(2,'IBM',3286,16,4444,6666)
        impressora = Impressora(1,'Printer',40)
        impressora2 = Impressora(21,'Printer',40)

        servidor.adicionar_impressora(impressora)
        servidor.adicionar_impressora(impressora2)
        servidor.impressoras |should| equal_to([impressora, impressora2])

        impressora.destruir_maquina()
        servidor.impressoras |should| equal_to([impressora2])

        impressora2.destruir_maquina()
        servidor.destruir_maquina()

        
if __name__ == "__main__":
    unittest.main()

