#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 16:44:43 2022

@author: aldo
"""

import socket 
import time
def scanner():
    
    # Prompt the user to scan ports.
    user = input('What do you want to scan? ')
    
    # Translate a host name to IPv4 address format. 
    IP = socket.gethostbyname(user)
    
    # Print the port being scanned. 
    print(f'Start the scan on host: {IP}')
    
    
    Begin = time.time()
    
    # Begin a for loop and using the time import with try and except 
    # scanning for 10 ports
    for port in range(11):
        try:
            # Using the import socket 
            so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conn = so.connect_ex((IP, port))
            if conn == 0:
                print(f'Your port {port} is open. ')
            so.close()
        except: 
            print(f'Your port {port} is closed. ')
            
            
    end = time.time()
    print(f'The time it took from {end-Begin:.2f} seconds')

if __name__=='__main__':
    scanner()


# I figured out why my print was printing out in negative time
# my original print was Beg-end when it should've been end-Beginning.     
    
    