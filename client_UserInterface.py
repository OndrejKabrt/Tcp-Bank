from Application import Applications
from Logger import log_input, log_output


class Client:
    def __init__(self, connection,client_address, server):
        self.connection = connection
        self.client_address = client_address
        self.server = server
        self.application = Applications(self, client_address)

    def run(self):
        while self.connection and self.server.server_socket:
            self.menu_input()

    def send_message(self, message, newline=True):
        if newline:
            message_as_bytes = bytes(message+"\n\r", "utf-8")
            log_output(message,self.client_address[0])
        else:
            message_as_bytes = bytes(message, "utf-8")
        self.connection.send(message_as_bytes)

    def menu_input(self):
        commands = [
            ("BC", self.application.bank_code),
            ("AC", self.application.account_create),
            ("AD", self.application.account_deposit),
            ("AW", self.application.account_withdraw),
            ("AB", self.application.account_balance),
            ("AR", self.application.account_remove),
            ("BA", self.application.bank_amount),
            ("BN", self.application.number_of_clients)
        ]

        command = None
        number = 0
        try:

            while command is None:
                command = self.get_input()
                try:
                    splited_command = command.split(" ", 1)
                    in_list_number = 0

                    for i in commands:
                        if i[0] == splited_command[0]:
                            number = in_list_number
                        else:
                            in_list_number += 1

                    if not (len(command) == 2):
                        return commands[number][1](splited_command[1])
                    else:
                        log_input(command, self.client_address[0])
                        return commands[number][1]()
                except Exception as e:
                    print("Tady")
                    self.send_message("ER Tento příkaz nesplňuje správný formát, nebo je špatně zadaný")
        except OSError:
            pass
        except ConnectionAbortedError:
            pass


    def terminate_client(self):
        self.connection.close()
        self.connection = None

    def get_input(self):
        buffer = b""

        while True:
            chunk = self.connection.recv(256)
            if(chunk == b""):
                pass
            buffer += chunk

            if buffer.endswith(b"\r\n"):
                message = buffer.decode("utf-8")
                return message.strip()