import socket
import threading
from client_UserInterface import Client

class Server:
    def __init__(self):
        server_inet_address =("127.0.0.1", 65430)

        server_socket = socket.socket()
        server_socket.bind(server_inet_address)
        server_socket.listen()

        self.server_socket = server_socket
        self.isrunning = True

        print("Server start on "+str(server_inet_address[0])+":"+str(server_inet_address[1]))

    def create_new_client(self, connection, server):
        c = Client(connection, server)
        c.run()


    def server_run(self):
        while self.isrunning:
            try:
                connection, client_address = self.server_socket.accept()
                thread = threading.Thread(target=self.create_new_client, args=(connection, self,))
                thread.start()
            except OSError:
                break
            except ConnectionAbortedError:
                break

if __name__ == "__main__":
    s = Server()
    s.server_run()