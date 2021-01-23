# This is shebang
#! /usr/bin/env python
#This is the example to use subprocess
import subprocess # This will import subprocess module
import optparse # The module to parse the arguments provided by the user

parser = optparse.OptionParser() # parser is the variable which returns the value by OptionParser
parser.add_option("-i", "--interface", dest="interface", help="Interface to change the MAC address") #Interface can be entered as i or interface and help is also available for that arguments
parser.add_option("-m", "--new_mac", dest="new_mac", help="New MAC address") # MAC address can be entered as m or new_mac and help is also available for that argument.
(options, arguments) = parser.parse_args() #i,m,interface or new_mac are called arguments and the value we enter is called options. parse_args are the argument that are provided by the user at the command line.

interface = options.interface
new_mac = options.new_mac
#Select all the lines and use ctrl + / which will change the code lines to comments.
# subprocess.call("ifconfig " + interface +  " down",shell=True) # Call function will run command and wait until the command is completed before running another line. shell=True will allow to run the sheel command.
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac ,shell=True) # Call function will run command and wait until the command is completed before running another line. shell=True will allow to run the sheel command.
# subprocess.call("ifconfig " + interface + " up",shell=True) # Call function will run command and wait until the command is completed before running another line. shell=True will allow to run the sheel command.

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

print("[+] Changing MAC address for " + interface + " and new MAC address of " + interface + " is " + new_mac )