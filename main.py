import sipfullproxy as sfp
import socket
import socketserver

def initGlobals(ip_addr):
  sfp.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ip_addr, sfp.PORT)
  sfp.topvia = "Via: SIP/2.0/UDP %s:%d" % (ip_addr, sfp.PORT)

def getHostIP():
  return socket.gethostbyname(socket.gethostname())

def runProxyServer():
  server = socketserver.UDPServer((sfp.HOST, sfp.PORT), sfp.UDPHandler)
  server.serve_forever()

if __name__ == "__main__":
  host_ip = getHostIP()
  initGlobals(host_ip)
  print("IP adresa SIP Proxy servera je: {}:{}\n".format(host_ip, sfp.PORT))
  runProxyServer()
