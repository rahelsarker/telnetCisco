import telnetlib
USERNAME = "cisco"
PASSWORD = "cisco"
HOST = "10.0.0.10"
print("USERNAME: ", USERNAME, "\nPASSWORD: ", PASSWORD)
connectTelnet = telnetlib.Telnet(HOST)
terminal = connectTelnet.read_until(b"Username:")
print(terminal.decode("ascii"))