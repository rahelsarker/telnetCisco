# Library for telnet connection
import telnetlib

# Constants
USERNAME = "cisco"
PASSWORD = "cisco"
HOST = "10.0.0.10"

# Initialize connection
connectTelnet = telnetlib.Telnet(HOST)

# Function for commands
def terminalConnect(terminalCommand, commandType):
	terminal = connectTelnet.read_until(commandType.encode('ascii'), 1)
	print( terminal.decode("ascii"))
	connectTelnet.write(terminalCommand.encode('ascii') + "\n".encode('ascii'))
	terminal = connectTelnet.read_until(commandType.encode('ascii'), 2)
	print(terminal.decode("ascii"))

# Command sequence
terminalConnect(USERNAME, ":")
terminalConnect(PASSWORD, ">")
terminalConnect("enable", ":")
terminalConnect(PASSWORD, "#")
terminalConnect("configure terminal", "#")
terminalConnect("vlan 50", "#")
terminalConnect("name VLAN50", "#")
terminalConnect("exit", "#")
terminalConnect("interface ethernet 1/0", "#")
terminalConnect("switchport trunk encapsulation dot1q", "#")
terminalConnect("switchport mode trunk", "#")
terminalConnect("switchport trunk allowed vlan all", "#")
terminalConnect("exit", "#")
terminalConnect("interface ethernet 2/0", "#")
terminalConnect("switchport mode access", "#")
terminalConnect("switchport access vlan 50", "#")
terminalConnect("exit", "#")

terminalConnect("end", "#")

# Close connection
connectTelnet.close()