import socket

try:
    s = socket.create_connection(("localhost", 3310), timeout=5)
    s.sendall(b"PING\n")
    response = s.recv(1024)
    print("Response:", response.decode())
    s.close()
except Exception as e:
    print("Connection failed:", e)