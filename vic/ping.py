#!/usr/bin/env python

import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import time
global ip
ip = '192.168.0.194'

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
    print( 'go')


def main():
    while True:
        if not ping(ip):
            time.sleep(1)
            print('Entrando en modo deteccion')
        else:
            accion()
            while True:
                response = ping(ip)
                time.sleep(1)
                if not response:
                    print('Hemos morido')
                    break
        

if __name__ == '__main__':
    main()

