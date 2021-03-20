#!/usr/bin/env python

import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import time

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0


def accion():
    return 'go'


def main():
    while True:
        if not ping('www.google.com'):
            time.sleep(10)
        else:
            accion()
            while True:
                response = ping()
                time.sleep(15)
                if not response:
                    print('Hemos morido')
                    break
        

