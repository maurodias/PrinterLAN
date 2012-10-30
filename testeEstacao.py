#!/usr/bin/env python
# -*- coding: utf-8 -*-
  
import unittest
from should_dsl import should, should_not
from maquina import Maquina
from computador import Computador
from estacao import Estacao
from usuario import Usuario

from servidor import Servidor
from impressora import Impressora
from impressao import Impressao


class testeEstacao(unittest.TestCase):

    def test_obter_estacao(self):
        estacao = Estacao(1,'DELL',4,512,'lab-8')
        
        estacao.localizacao |should| equal_to('lab-8')
        estacao.usuario |should| equal_to('Livre')
        
        estacao.destruir_maquina()


    def test_alterar_estacao(self):
        estacao = Estacao(1,'DELL',4,512,'lab-8')
        
        estacao.localizacao = 'lab-7'
        estacao.localizacao |should| equal_to('lab-7')
        
        estacao.destruir_maquina()
        
    
if __name__ == "__main__":
    unittest.main()

