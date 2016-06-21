import socket

connection_with_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection_with_server.connect(('localhost', 9999))

get_msg = connection_with_server.recv(1024)
get_msg