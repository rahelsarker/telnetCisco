import telnetlib
USERNAME = "cisco"
PASSWORD = "cisco"
HOST = "10.0.0.10"
#print("USERNAME: ", USERNAME, "\nPASSWORD: ", PASSWORD)
connectTelnet = telnetlib.Telnet(HOST)
terminal = connectTelnet.read_until(":".encode('ascii'), 2)

def terminalConnect(terminalCommand):
	connectTelnet.write(USERNAME.encode('ascii') + "\n".encode('ascii'))
	terminal = connectTelnet.read_until(b"#", 2)
	print(terminal.decode("ascii"), terminalCommand)

terminalConnect(USERNAME.encode('ascii'))

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