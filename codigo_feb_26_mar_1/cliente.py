"""
Ejemplo de socket para un cliente
"""

import socket
import sys

HOST = "localhost"  # 127.0.0.1

if len(sys.argv) == 2:
    puerto = int(sys.argv[1])
    print("Puerto: ", puerto)

    sock_c = None
    try:
        # Crea un socket para el cliente:
        sock_c = socket.socket()

        # Se conecta con el servidor:
        sock_c.connect((HOST, puerto))

        while True:
            mensaje = input("Mensaje> ")
            if mensaje == "":
                continue

            # Enviamos un mensaje al server:
            sock_c.send(mensaje.encode("utf-8"))

            if mensaje.lower() == "fin":
                break

            # Esperar el mensaje del Servidor:
            mensajeSer = sock_c.recv(1024)
            mensajeSer = mensajeSer.decode("utf-8")
            print("El Server dice: ", mensajeSer)

    except Exception as e:
        print("ERROR", e)

    except KeyboardInterrupt as e:
        print("Interrupcion de teclado")
        sock_c.send("fin".encode("utf-8"))

    finally:
        if sock_c != None:
            sock_c.close()

else:
    print("No se ha indicado el puerto")
