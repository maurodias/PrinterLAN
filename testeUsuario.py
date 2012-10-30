#!/usr/bin/env python
# -*- coding: utf-8 -*-
  
import unittest
from should_dsl import should, should_not
from usuario import Usuario
from estacao import Estacao

class testeUsuario(unittest.TestCase):

    def test_obter_nome(self):
        usuario = Usuario('diego','xxx')
        usuario.nome |should| equal_to('diego')
        usuario.apagar_usuario()
        
        
    def test_obter_senha(self):
        usuario = Usuario('diego','xxx')
        usuario.senha |should| equal_to('xxx')
        usuario.apagar_usuario()


    def test_alterar_nome(self):
        usuario2 = Usuario('rodolfo','123456')
        (usuario2._verificar_identidade, 'rodolfo') |should| throw(ValueError)
        usuario2.nome = 'mauro'
        usuario2.nome |should| equal_to('mauro')    
        (usuario2._verificar_identidade,'rodolfo') |should_not| throw(ValueError)
        usuario2.apagar_usuario()
        
           
    def test_alterar_senha(self):
        usuario2 = Usuario('diego','xxx')
        usuario2.senha = "54321"
        usuario2.senha |should| equal_to('54321')
        usuario2.apagar_usuario()
    
    
    def test_usuario_logar_deslogar(self):
        estacao = Estacao(1,'DELL',4,512,'lab-8')
        usuario = Usuario('mauro','maurodias')
        
        usuario.logar(estacao)
        
        estacao.usuario |should| equal_to(usuario)
        usuario.atual_estacao |should| equal_to(estacao)
        
        (estacao._verificar_disponibilidade) |should| throw(ValueError)
        (usuario._verificar_disponibilidade) |should| throw(ValueError)
        estacao.usuario |should| equal_to(usuario)
        (estacao.destruir_maquina) |should| throw(ValueError)
        
        usuario.deslogar()
       
        estacao.destruir_maquina()        
        usuario.apagar_usuario()

        
if __name__ == "__main__":
    unittest.main()

