#!/usr/bin/env python
# -*- coding: utf-8 -*-
  
import unittest
from should_dsl import should, should_not
from maquina import Maquina
from impressora import Impressora

class testeImpressora(unittest.TestCase):

    def test_obter_impressora(self):
        impressora = Impressora(20,'Printer',40,'maquina1')
        impressora.velocidade |should| equal_to(40)
        impressora.host |should| equal_to('maquina1')
        Maquina.destruir_maquina(impressora)
        

    def test_alterar_impressora(self):
        impressora = Impressora(20,'Printer',40,'maquina1')
        (impressora._validar_valor_positivo,1) |should_not| throw(ValueError)
        (impressora._validar_valor_positivo,0) |should| throw(ValueError)
        impressora.velocidade = 102    
        impressora.velocidade |should| equal_to(102)
        impressora.host = 'host2'
        impressora.host |should| equal_to('host2')
        Maquina.destruir_maquina(impressora)      
          
          
          
if __name__ == "__main__":
    unittest.main()

