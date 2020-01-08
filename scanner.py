# coding:utf-8
import socket


def port_ouvert(adresseip):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        for port in range(0,100):
                if sock.connect_ex((adresseip, port)) == 0:
                        print ("Le port", port, "est ouvert")
                        
def cent_premier_port(adresseip):
        print ("------------")
        for port in range(1, 100):
                if sock.connect_ex((adresseip, port)):
                        print ("Le port", port, "est fermé")
                else:
                        print ("Le port", port, "est ouvert")
        print ("------------")

def check_port(adresseip, port):
        print ("------------")
        if sock.connect_ex((adresseip, port)):
                print ("Le port", port, "est fermé")
        else:
                print ("Le port", port, "est ouvert")
        print ("------------")


# Main Prg --------------------------------------------------------

adresseip = input("Entrez une adresse IP : ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4 TCP
print("Tapez 1 : pour checker les cent premier port")
print("Tapez 2 : pour choisir un port ")
choix = int(input("$> "))
if choix == 1:
        cent_premier_port(adresseip)
elif choix == 2:
        port = int(input("Entrez un numéro de port : "))
        check_port(adresseip, port)
else:
        print("T'es CON ou t'es CON !!! je t'es dis sois 1 ou 2 et toi comme un con tu prends", choix)


