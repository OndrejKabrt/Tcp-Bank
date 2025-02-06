import json
import socket

from Logger import log_user
from client_UserInterface import Client
import multiprocessing.process

class Server:
    def __init__(self):

        with open('ipConfig.json', 'r') as f:
            config = json.load(f)

        host = config['IP']['host']
        port = config['IP']['port']
        timeout = config['IP']['timeout']

        server_inet_address =(host, port)

        server_socket = socket.socket()
        server_socket.bind(server_inet_address)
        server_socket.settimeout(timeout)
        server_socket.listen()

        self.server_socket = server_socket
        self.isrunning = True

        print("Server start on "+str(server_inet_address[0])+":"+str(server_inet_address[1]))

    def create_new_client(self, connection,client_address, server):
        c = Client(connection,client_address, server)
        c.run()

    def server_run(self):
        while self.isrunning:
            try:
                connection, client_address = self.server_socket.accept()
                thread = multiprocessing.Process(target=self.create_new_client, args=(connection,client_address, self,))
                print(f"Client connected from {client_address[0]}")
                log_user(client_address[0])
                thread.start()
            except socket.timeout:
                continue
            except OSError:
                break
            except ConnectionAbortedError:
                break


if __name__ == "__main__":
    s = Server()
    s.server_run()