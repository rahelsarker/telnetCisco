import telnetlib
USERNAME = "cisco"
PASSWORD = "cisco"
HOST = "10.0.0.10"
#print("USERNAME: ", USERNAME, "\nPASSWORD: ", PASSWORD)
connectTelnet = telnetlib.Telnet(HOST)

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

#if b"Username" in terminal:
#	connectTelnet.write(USERNAME.encode('ascii') + "\n".encode('ascii'))
#	terminal = connectTelnet.read_until(b":", 2)
#	connectTelnet.write(PASSWORD.encode('ascii') + "\n".encode('ascii'))
#	terminal = connectTelnet.read_until(b">", 2)
#	print("Login Success\n", terminal.decode("ascii"))
#	connectTelnet.write(b"enable" + b"\n")
#	terminal = connectTelnet.read_until(b":", 2)
#	if b"Password:" in terminal:
#		connectTelnet.write(PASSWORD.encode('ascii') + "\n".encode('ascii'))
#	else:
#		print(terminal.decode("ascii"))
#	connectTelnet.write(b"configure terminal" + b"\n")
#	terminal = connectTelnet.read_until(b"#", 2)
#	print(terminal.decode("ascii"))
#else:
#	print(terminal.decode("ascii"))