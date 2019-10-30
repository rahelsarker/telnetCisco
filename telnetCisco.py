import telnetlib
USERNAME = "cisco"
PASSWORD = "cisco"
HOST = "10.0.0.10"
#print("USERNAME: ", USERNAME, "\nPASSWORD: ", PASSWORD)
connectTelnet = telnetlib.Telnet(HOST)
terminal = connectTelnet.read_until(":".encode('ascii'))

if "Username".encode('ascii') in terminal:
	connectTelnet.write(USERNAME.encode('ascii') + "\n".encode('ascii') + PASSWORD.encode('ascii'))
	terminal = connectTelnet.read_until(">".encode('ascii'))
	print("Login Success\n", terminal.decode("ascii"))
else:
	print(terminal.decode("ascii"))