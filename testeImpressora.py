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
       
        (impressora._validar_valor_positivo,1) |should_not| throw(ValueError)
        (impressora._validar_valor_positivo,0) |should| throw(ValueError)

        impressora.velocidade |should| equal_to(40)
        impressora.host |should| equal_to(None)

        impressora.destruir_maquina()        
       
        
    def test_adicionar_remover_host(self):        
        server = Servidor(19,'IBM',3286,16,4444,6666)
        impressora = Impressora(20,'Printer',40)
        
        impressora.adicionar_host(server)
        impressora.host |should| equal_to(server)

        (impressora.adicionar_host, server) |should| throw(ValueError)     
     
        impressora.remover_host()
        impressora.host |should| equal_to(None)           
        
        impressora.destruir_maquina()
        server.destruir_maquina()
        
        
    def test_alterar_impressora(self):
        impressora = Impressora(5,'Printer',40)
        
        impressora.velocidade = 102    
        impressora.velocidade |should| equal_to(102)
        
        impressora.destruir_maquina()      
        
          
    def test_destruir_host(self):
        servidor = Servidor(19,'IBM',3286,16,4444,6666)
        impressora = Impressora(20,'Printer',40)
        
        servidor.adicionar_impressora(impressora)
        impressora.host |should| equal_to(servidor) 

        (servidor.destruir_maquina)|should| throw(ValueError)     
        servidor.desconectar_todas_impressoras()
        (servidor.destruir_maquina)|should_not| throw(ValueError) 

        impressora.host |should| equal_to(None)
       
        impressora.destruir_maquina()
          
if __name__ == "__main__":
    unittest.main()

