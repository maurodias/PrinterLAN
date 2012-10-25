#!/usr/bin/env python
# -*- coding: utf-8 -*-
  
import unittest
from should_dsl import should, should_not
from maquina import Maquina
from servidor import Servidor
from impressora import Impressora

class testeImpressora(unittest.TestCase):

    def test_obter_impressora(self):
        impressora = Impressora(10,'Printer',40)
        impressora.velocidade |should| equal_to(40)
        impressora.host |should| equal_to(None)
        impressora.destruir_maquina()        
        
    def test_adicionar_host(self):        
        server = Servidor(19,'IBM',3286,16,4444,6666)
        impressora = Impressora(20,'Printer',40)
        
        impressora.adicionar_host(server)
        impressora.host |should| equal_to(server)

        impressora2 = Impressora(21,'Printer2',40)
        impressora2.adicionar_host(server)
        (server.verificar_disponibilidade) |should_not| throw(ValueError)        
        
        impressora3 = Impressora(22, 'Printer3',40)
        (impressora3.adicionar_host,impressora2) |should| throw(ValueError)
        
        impressora3.adicionar_host(server)
        impressora3.host |should| equal_to(server)
        (server.verificar_disponibilidade) |should| throw(ValueError)
           
        impressora.destruir_maquina()   
        impressora2.destruir_maquina()  
        impressora3.destruir_maquina()  
        server.destruir_maquina() 
    
    def test_remover_host(self):
        server = Servidor(19,'IBM',3286,16,4444,6666)
        impressora = Impressora(20,'Printer',40)
        
        impressora.host |should| equal_to(None)
        (impressora.remover_host) |should| throw(ValueError)
        
        impressora.adicionar_host(server)
        impressora.host |should| equal_to(server) 
        impressora.remover_host()
        impressora.host |should| equal_to(None)           
        
        
        impressora.destruir_maquina()
        server.destruir_maquina()
        
    def test_alterar_impressora(self):
        impressora = Impressora(5,'Printer',40)
        (impressora._validar_valor_positivo,1) |should_not| throw(ValueError)
        (impressora._validar_valor_positivo,0) |should| throw(ValueError)
        impressora.velocidade = 102    
        impressora.velocidade |should| equal_to(102)
        impressora.destruir_maquina()      
          
          
          
if __name__ == "__main__":
    unittest.main()

