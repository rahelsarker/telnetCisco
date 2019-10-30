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
	terminal = connectTelnet.read_until(commandType.encode('ascii'), 2)
	print( terminal.decode("ascii"))
	connectTelnet.write(terminalCommand.encode('ascii') + "\n".encode('ascii'))
	terminal = connectTelnet.read_until(commandType.encode('ascii'), 2)
	print(terminal.decode("ascii"))

terminalConnect(USERNAME, ":")
terminalConnect(PASSWORD, ">")
terminalConnect("enable", ":")
terminalConnect(PASSWORD, "#")
terminalConnect("configure terminal", "#")
terminalConnect("vlan 100", "#")
terminalConnect("name VLAN100", "#")
terminalConnect("exit", "#")
