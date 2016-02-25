# -*- coding: utf-8 -*-
u"""Este pequeno módulo serve para iniciar o docker em caso de parada.

Para isto, basta enviar id do container ativo para monitorar, e cadastrar
este script no cron.

OBS: os prints abaixo servem para logar o que está acontecendo no log
do crontab
"""
from commands import getstatusoutput


class ContainerAutoStart(object):
    u"""Reinicia docker automaticamente em caso de parada."""

    def __init__(self, container_id):
        u"""container_id deve ser uma string contendo o ID do container."""
        self.container_id = container_id

    def supervisor(self):
        u"""Processo responsável por verificar se docker está rodando."""
        ps = getstatusoutput("docker ps")
        if 0 in ps:
            if self.container_id not in ps[1]:
                print "Reiniciando Docker"
                self.start_container()
            else:
                print "Docker rodando normalmente"

    def start_container(self):
        u"""Processo deve ser invocado para iniciar o container."""
        ct_id = self.container_id
        ps = getstatusoutput("docker start {}".format(ct_id))
        if ct_id not in ps:
            self.supervisor()
        else:
            print "Docker iniciado com sucesso"


# Exemplo de uso
if __name__ == "__main__":
    dk = ContainerAutoStart("97ebaea37f47")
    dk.supervisor()
