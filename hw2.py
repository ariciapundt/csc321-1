#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 19:00:53 2023

@author: ariciapundt
"""

import netifaces as ni
import ipaddress



def get_interfaces():
    """in terminal i use ifconfig for this"""
    return ni.interfaces()

def get_mac(interface):
    """"getting mac address for the interface"""
    interfaces = ni.interfaces()
    mac_address = ni.ifaddresses(interface)[ni.AF_LINK] ##getting mac address
    return mac_address
    

def get_ips(interface):
    ip_dict = {}
    try:
        addrs6 = ni.ifaddresses(interface)
        ip = addrs6[ni.AF_INET6][0]['addr'] #AF_INET6 lets you get the ipv6 address
        ip_dict['ipv6'] = ip
    except: 
        pass
    try:
        addrs4 = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']
        ip = addrs4[ni.AFINET][0]['addr'] #AFINET lets you get ipv4
        ip_dict['ipv4'] = ip
    except:
        pass
    return ip_dict

def get_netmask(interface):
    netmask_dict = {}
    try:
        addrs6 = ni.ifaddresses(interface)
        ip6 = addrs6[ni.AF_INET6][0]['netmask'] #'netmask' key pulls the netmask addr for ipv6
        netmask_dict['ipv6'] = ip6
    except:
        print('no netmask')
        
    try:
        addrs4 = ni.ifaddresses(interface)
        ip4 = addrs4[ni.AF_INET][0]['netmask'] #'netmask' key here is pulling netmask for ipv4
        netmask_dict['ipv4'] = ip4
    except:
        print('no netmask 4')
        
    return netmask_dict
        
        
def get_network(interface):
    network_dict = {}
    try:
        address = ni.ifaddresses(interface)
        ip6 = address[ni.AF_INET6][0]['netmask']
        network_dict['v6'] = ip6
    except:
         pass
    
    try:
        address = ni.ifaddresses(interface)
        ip4 =  address[ni.AF_INET][0]['broadcast']
        network_dict['v4'] = ip4
    except:
        pass
    
    return network_dict
     
        

        
        