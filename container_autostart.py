# -*- coding: utf-8 -*-
u"""This small module is usefull to monitor docker process and if it stops, we
can automatically restart it.

For this, we should send id of the active container to monitoring, and set 
the script on the crontab.

PS: The print statement is only to log what is happening, we probably will 
fix it to the future log tool.
"""
from commands import getstatusoutput


class ContainerAutoStart(object):
    u"""Auto restart container if stop cases."""

    def __init__(self, container_id):
        u"""container_id should be a string with the ID."""
        self.container_id = container_id

    def supervisor(self):
        u"""Check if docker is running."""
        ps = getstatusoutput("docker ps")
        if 0 in ps:
            if self.container_id not in ps[1]:
                print "Restarting Docker"
                self.start_container()
            else:
                print "Docker is running now"

    def start_container(self):
        u"""Start the container based on container id provided."""
        ct_id = self.container_id
        ps = getstatusoutput("docker start {}".format(ct_id))
        if ct_id not in ps:
            self.supervisor()
        else:
            print "Docker started"


# How to use it.
if __name__ == "__main__":
    dk = ContainerAutoStart("97ebaea37f47")
    dk.supervisor()
