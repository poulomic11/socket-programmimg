import socket
import os                   # Import socket module

port = 80                # Reserve a port for your service.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
#host = '192.168.1.1'     # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print ('Server listening....')
conn, addr = s.accept() 
message = "Hello"
while True:
    conn.send(bytes(message,'utf-8'))
    print("message sent!")

#data = bytes(s.recv(1024),'utf-8')
#print("received message: %s"%data)

#while True:
    #print("KK")
 #   conn, addr = s.accept()     # Establish connection with client.
  #  print ('Got connection from', addr)
    #data = conn.recv(1024)
    #print('Server received', repr(data))

    #filename='mytext.txt'
    #f = open(filename,'rb')
    #l = f.read(1024)
    #while (l):
    #   conn.send(l)
    #   print('Sent ',repr(l))
    #   l = f.read(1024)
    #f.close()




   

print('Done sending')
#ol    conn.send('Thank you for connecting')
conn.close()