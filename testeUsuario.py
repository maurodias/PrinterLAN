#!/usr/bin/env python
# -*- coding: utf-8 -*-
  
import unittest
from should_dsl import should, should_not
from usuario import Usuario

class testeUsuario(unittest.TestCase):

    def test_obter_nome(self):
        usuario = Usuario('diego','didimax')
        usuario.nome |should| equal_to('diego')
        usuario.apagar_usuario()
        
    def test_obter_senha(self):
        usuario = Usuario('diego','didimax')
        usuario.senha |should| equal_to('didimax')
        usuario.apagar_usuario()

    def test_alterar_nome(self):
        usuario2 = Usuario('rodolfo','123456')
        (usuario2._verificar_identidade, 'rodolfo') |should| throw(ValueError)
        usuario2.nome = 'mauro'
        usuario2.nome |should| equal_to('mauro')    
        (usuario2._verificar_identidade,'rodolfo') |should_not| throw(ValueError)
        usuario2.apagar_usuario()
        
    def test_alterar_senha(self):
        usuario2 = Usuario('diego','didimax')
        usuario2.senha = "54321"
        usuario2.senha |should| equal_to('54321')
        usuario2.apagar_usuario()
        
if __name__ == "__main__":
    unittest.main()

