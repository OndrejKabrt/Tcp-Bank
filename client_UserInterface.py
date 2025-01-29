

class Client:
    def __init__(self, connection, server):
        self.connection = connection
        self.server = server

    def run(self):
        while self.connection and self.server.server_socket:
            self.menu_input()

    def print_line(self):
        self.send_message(50*"=")

    def send_message(self, message, newline=True):
        if newline:
            message_as_bytes = bytes(message+"\n\r", "utf-8")
        else:
            message_as_bytes = bytes(message, "utf-8")
        self.connection.send(message_as_bytes)

    def menu_input(self):
        commands = [
            ("BC", self.bank_code())
        ]
        self.print_line()
        self.send_message("Choose a command:")

        number = 0
        for label, command in commands:
            number += 1
            self.send_message(f"{number}: {label}")

        command = None
        try:
            while command is None:
                self.send_message(f"Write command you want to execute: ", False)
                command = input() #Todo Parser
                try:
                    splited_command = command.split(" ", 1)

                except:
                    self.send_message("Invalid command")
                    command = None
        except OSError:
            pass
        except ConnectionAbortedError:
            pass
        else:
            return command[command - 1][1]()

    def terminate_client(self):
        self.connection.close()
        self.connection = None

    def get_help(self):
        help = []

        for label, desc in help:
            self.send_message(f"{label}: {desc}")
    def bank_code(self):
        return self.send_message("BC " + self.connection)