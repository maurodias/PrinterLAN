#!/usr/bin/env python
# -*- coding: utf-8 -*-
  
import unittest
from should_dsl import should, should_not
from maquina import Maquina
from computador import Computador

class testeComputador(unittest.TestCase):

    def test_obter_computador(self):
        computador = Computador(1,'PC',512,4088)
        computador.hd |should| equal_to(512)
        computador.memoria |should| equal_to(4088)
        computador.destruir_maquina()
        

    def test_alterar_computador(self):
        computador = Computador(1,'PC',512,4088)
        (computador._validar_valor,0) |should_not| throw(ValueError)
        (computador._validar_valor,-1) |should| throw(ValueError)
        computador.hd = 1024    
        computador.hd |should| equal_to(1024)
        computador.memoria = 1025
        computador.memoria |should| equal_to(1025)
        computador.destruir_maquina()        
if __name__ == "__main__":
    unittest.main()

