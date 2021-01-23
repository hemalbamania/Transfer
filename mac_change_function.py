# This is shebang
#! /usr/bin/env python
#This is the example to use subprocess
import subprocess # This will import subprocess module
import optparse # The module to parse the arguments provided by the user
def mac_change(interface, new_mac): #We are defining new function called mac_change with new input interface and new_mac
    subprocess.call(["ifconfig", interface, "down"])#Once the function is defined the code after that will start with indentation that indicates that code belongs to above function.
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print("[+] Changing MAC address for " + interface + " and new MAC address of " + interface + " is " + new_mac)

parser = optparse.OptionParser() # parser is the variable which returns the value by OptionParser
parser.add_option("-i", "--interface", dest="interface", help="Interface to change the MAC address") #Interface can be entered as i or interface and help is also available for that arguments
parser.add_option("-m", "--new_mac", dest="new_mac", help="New MAC address") # MAC address can be entered as m or new_mac and help is also available for that argument.
(options, arguments) = parser.parse_args() #i,m,interface or new_mac are called arguments and the value we enter is called options.

interface = options.interface
new_mac = options.new_mac
mac_change(options.interface, options.new_mac)

