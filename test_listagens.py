#!/usr/bin/env python
# -*- coding: utf-8 -*-
  
import unittest
from should_dsl import should, should_not
from maquina import Maquina
from estacao import Estacao
from servidor import Servidor
from impressora import Impressora
from usuario import Usuario
from impressao import Impressao

class testePrincipal(unittest.TestCase):  
        
    def test_listar_impressoes_impressora_TRUNCATING(self):
        usuario2 = Usuario('fabio','123456')
        Impressora.mostrar_fila() |should| equal_to('Nenhuma impressora') 
        impressora = Impressora(20,'Printer',40)
        impressao = Impressao('arquivo3.txt',impressora, usuario2,40)        
        Impressora.mostrar_fila() |should_not| equal_to('Nenhuma impressora')
        impressora.linha_lista(impressora,impressao) |should| equal_to('| arquivo3.txt                     | fabio                           |')
        impressora.imprimir()
        
        #truncate
        usuario = Usuario('Luiz Mauro Piraciaba Cassiano Dias','123456')
        impressao = Impressao('Relatorio unico de surpresa do dia de agosto do ano 2012.txt',impressora, usuario,10)        
        impressora.linha_lista(impressora,impressao) |should| equal_to('| Relatorio unico de surpresa d... | Luiz Mauro Piraciaba Cassiano...|')
        impressora.imprimir()
        
        usuario.apagar_usuario()
        usuario2.apagar_usuario()
        impressora.destruir_maquina()
                       
#  
#para cada estação
#código e caso exista, o nome do usuário conectado, a data e hora início desta conexão e, se houver, nome e quantidade de cópias dos arquivos que ele enviou e que ainda estão aguardando impressão.
#  def test_listar_estacoes_usuarios(self):
#        
#        impressora = Impressora(20,'Printer',40)
#        usuario = Usuario('diego','123456')
#        estacao = Estacao(1,'DELL',4,512,'lab-8')
#        usuario.logar(estacao)
#        servidor = Servidor(2,'PC',512,4088,128,10000)
#        servidor.adicionar_impressora(impressora)
#        impressao = Impressao('arquivo.txt',impressora, usuario,10)        

##        impressora.linha_lista(impressora,impressao) |should| equal_to('| arquivo3.txt                     | fabio                           |')
#        
#    

#        impressora.imprimir()
#        usuario.apagar_usuario()
#        servidor.desconectar_todas_impressoras()
#        impressora.destruir_maquina()
#        estacao.destruir_maquina()        
#        servidor.destruir_maquina()
        
            
if __name__ == "__main__":
    unittest.main()

