#!/usr/bin/env python
# -*- coding: utf-8 -*-
  
import unittest
from should_dsl import should, should_not
from maquina import Maquina

class testeMaquina(unittest.TestCase):

    def test_obter_codigo(self):
        maquina = Maquina(1,'PC')
        maquina.codigo |should| equal_to(1)
        maquina.destruir_maquina()
        
    def test_obter_descricao(self):
        maquina = Maquina(1,'PC')
        maquina.descricao |should| equal_to('PC')
        maquina.destruir_maquina()

    def test_alterar_codigo(self):
        maquina2 = Maquina(2,'PC2')
        (maquina2._verificar_identidade,2) |should| throw(ValueError)
        maquina2.codigo = 0    
        maquina2.codigo |should| equal_to(0)    
        (maquina2._verificar_identidade,2) |should_not| throw(ValueError)
        maquina2.destruir_maquina()
        
    def test_alterar_descricao(self):
        maquina2 = Maquina(2,'PC2')
        maquina2.descricao = "Lenovo"
        maquina2.descricao |should| equal_to('Lenovo')
        maquina2.destruir_maquina()
        
if __name__ == "__main__":
    unittest.main()

