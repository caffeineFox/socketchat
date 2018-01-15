__author__ = 'fabianpfingst'

import socket

ip = "192.168.178.21"   # serverIP eintragen (ipv4)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # erstellt Client-Socket
s.connect((ip, 50000)) # schickt Verbindungsanfrage an IP über Server-Adresse an Server-Socket

try:
    print("Verbunden!\n")
    while True:
        nachricht = input("Nachricht: ") # Nachrichteneingabe
        s.send(nachricht.encode()) # wartet nach dem Senden an Server-Socket auf Nachricht von Server-Socket
        antwort = s.recv(1024) # empfängt Nachricht von Server-Socket
        print("[%s] %s" % (ip, antwort.decode())) # gibt Nachricht und IP-Adresse von Server-Socket aus
finally:
    s.close() # entfernt Client-Socket