__author__ = 'fabianpfingst'

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # erstellt Server-Socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("", 50000)) # bindet Server-Socket an Adresse
s.listen(1) # wartet auf eingehende Anfrage (von Client-Socket)

try:
    while True:
        komm, addr = s.accept() # nimmt Verbindung und Client-Adresse entgegen
        while True:
            data = komm.recv(1024) # empfängt Nachricht von Client-Socket

            if not data:
                komm.close() # schließt Verbindung
                break

            print("[%s] %s" % (addr[0], data.decode())) # gibt Nachricht und IP von Client aus
            nachricht = input("Antwort: ") # Antworteingabe
            komm.send(nachricht.encode()) # sendet Nachricht an Client, geht zu recv und wartet auf einkommende Nachricht aus Client-Socket
finally:
    s.close() # entfernt Socket