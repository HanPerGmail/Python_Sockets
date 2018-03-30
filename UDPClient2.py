from socket import *
import threading
import time

class PingerThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run (self):
        for i in range(10):
          print ('start thread')
          cs = socket(AF_INET, SOCK_DGRAM)
          cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
          cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
          cs.bind(('0.0.0.0', 30303))
          msgFromServer = cs.recvfrom(1024)
          msgFromServer2 = cs.recvfrom(1024)
          msg = "Message from Server {}".format(msgFromServer[0])
          msg2 = "Message  2from Server {}".format(msgFromServer2[0])
          print(msg)
          print(msg2)
          time.sleep(1)

a = PingerThread() 
a.start()


cs = socket(AF_INET, SOCK_DGRAM)
cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
try:
    cs.bind(('0.0.0.0', 30303))
    cs.sendto("Discovery: Who is out there?\0\n".encode(), ("192.168.14.255", 30303))
except:
    print ('failed to bind')
    cs.close()
    raise
    cs.blocking(0)
time.sleep(1)

