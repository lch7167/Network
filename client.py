import socket
from threading import Thread
ip= input("ip주소 :")
HOST = ip
PORT = int(input("포트번호를 입력해주세요 : "))
 
def rcvMsg(sock):
   while True:
      try:
         data = sock.recv(1024)
         if not data:
            break
         print(data.decode())
      except:
         pass
 
def runChat():
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
      sock.connect((HOST, PORT))
      t = Thread(target=rcvMsg, args=(sock,))
      t.daemon = True
      t.start()
 
      while True:
         msg = input()
         if msg =='/quit':
            sock.send(msg.encode())
            break
 
         sock.send(msg.encode())
             
runChat()
