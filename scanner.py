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

def intervalle_de_port(a,b):
        print ("------------")
        for port in range(a, b):
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
print("Tapez 2 : pour choisir une intervalle de port")
print("Tapez 3 : pour choisir un port precis")
choix = int(input("$> "))
if choix == 1:
        cent_premier_port(adresseip)
elif choix == 2:
        print("Veilliez saisir un intervalle a et b, tel que  a<=b ")
        a = int(input("$> a = "))
        b = int(input("$> b = "))
        if b<a:
                print("T'es CON ou t'es CON ??? b doit être supérieur à a")
        else:
                intervalle_de_port(a,b)
        
elif choix == 3:
        port = int(input("Entrez un numéro de port : "))
        check_port(adresseip, port)
else:
        print("T'es CON ou t'es CON !!! je t'es dis sois 1, 2 ou 3, et toi comme un con tu prends", choix)


