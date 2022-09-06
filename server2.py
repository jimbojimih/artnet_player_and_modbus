import socket
HOST = "localhost"  
PORT = 6454        
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        #print('Connected by', addr)
        
        while True:
            data = conn.recv(4096)
            #print(data[0:9])
            #print(data[14])
            #if not data:
             #   break
            
            #conn.sendall(data)