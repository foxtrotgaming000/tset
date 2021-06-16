#!/usr/bin/python

import subprocess, optparse, re

def get_args():

    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='Interface to Change MAC Address')
    parser.add_option('-m', '--mac', dest='new_mac', help='MAC Address You Want To Change')
    (options, arguments) = parser.parse_args()
	
    if not options.interface and not options.new_mac:
	    parser.error('[*] Please Specify an Interface an a MAC Address, use "-h" for more info.')
    if not options.interface:
        parser.error('[*] Please Specify an Interface, use "-h" for more info.')
    if not options.new_mac:
        parser.error('[*] Please Specify a MAC Address, use "-h" for more info.')
    return options
		 	

def change_mac(interface, new_mac):

    print('changing mac of interface ' + interface + ' > ' + new_mac)

    subprocess.call('ifconfig | grep "ether" >> old_ether.txt', shell=True)  # Saves old ether
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])

def get_mac(interface):
    
    ifconfig_result = subprocess.check_output(['ifconfig', interface], encoding='utf8')
    mac_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result)
    if mac_result:
        print('current mac > ', mac_result.group(0))
        return mac_result.group(0)
    else:
        print('[*] Couldn\'t read MAC address')
    
options = get_args()

current_mac = get_mac(options.interface)

change_mac(options.interface, options.new_mac)

current_mac = get_mac(options.interface)

if current_mac == options.new_mac:
    print('> Success')
else:
    print('> Failure')
