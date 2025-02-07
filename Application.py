import random
import re
import socket

from Account import Account
from AccountDAO import AccountDAO


class Applications:

    def __init__(self, client, client_address):
        self.client = client
        self.client_address = client_address
        self.account_Dao = AccountDAO()
        self.ip = str(self.client.connection).split("laddr=('")[1].split("',")[0]


    def bank_code(self):
        return self.client.send_message("BC " + self.client_address[0])

    def account_create(self, accountdata = None):
        try:
            if accountdata:
                raise Exception
            all_accounts = self.account_Dao.select_all()
            if not all_accounts:
                all_accounts = []
            new_account = random.choice([i for i in range(10000, 99999) if i not in all_accounts])
        except Exception:
            self.client.send_message("ER Naše banka nyní neumožňuje založení nového účtu.")
        else:
            account = Account(int(new_account), 0)
            self.account_Dao.save(account)

            return self.client.send_message(f"AC {new_account}/{self.ip}")

    def account_deposit(self, accountdata):
        try:
            account_number_and_ip, currency = accountdata.split(' ')
            if not bool(re.search(r'[+-]', currency)):
                account_number, ip_address = account_number_and_ip.split('/')
                if re.fullmatch(str(self.ip), str(ip_address)):
                        all_accounts = self.account_Dao.select_all()
                        for account in all_accounts:
                            if re.fullmatch(str(account_number),str(account.account_number)):
                                increse = Account(account.account_number, currency)
                                self.account_Dao.update_positive(increse)
                                return self.client.send_message(f"AD")
                else:
                    input = f"AD {accountdata}"
                    dif_srv_ans = self.command_redirection(input)
                    return dif_srv_ans
                    pass
        except Exception as e:
            print(e)
        else:
            return self.client.send_message("ER číslo bankovního účtu a částka není ve správném formátu.")






    def account_withdraw(self, accountdata):
        account_number_and_ip, currency = accountdata.split(' ')
        if not bool(re.search(r'[+-]', currency)):
            account_number, ip_address = account_number_and_ip.split('/')
            if re.fullmatch(str(self.ip), str(ip_address)):
                try:
                    found = 0
                    all_accounts = self.account_Dao.select_all()
                    for account in all_accounts:
                        if re.fullmatch(str(account_number),str(account.account_number)):
                            found = 1
                            if int(currency) <= int(account.currency):
                                decrese = Account(account.account_number, currency)
                                self.account_Dao.update_negative(decrese)
                                self.client.send_message(f"AW")
                            else:
                                self.client.send_message(f"ER učet nemá požadovanou výši finančních prostředků")
                    if found == 0:
                        self.client.send_message(f"ER zadané číslo účtu není v databázi.")

                except:
                    self.client.send_message(f"ER číslo bankovního účtu a částka není ve správném formátu.")
            else:
                input = f"AW {accountdata}"
                dif_srv_ans = self.command_redirection(input)
                return dif_srv_ans
                pass
        else:
            self.client.send_message(f"ER číslo bankovního účtu a částka není ve správném formátu.")


    def account_balance(self, accountdata):
        account_number, ip_address = accountdata.split('/')
        if (int(account_number) >= 10000 and int(account_number) <= 99999) :
            if re.fullmatch(str(self.ip), str(ip_address)):
                all_accounts = self.account_Dao.select_all()
                for account in all_accounts:
                    if re.fullmatch(str(account_number),str(account.account_number)):
                        balance = self.account_Dao.select_balance(account_number)
                        currency = balance[0][0]
                        return self.client.send_message(f"AB {currency}")
            else:
                try:
                    input = f"AB {accountdata}"
                    dif_srv_ans = self.command_redirection(input)
                    return self.client.send_message(f"{dif_srv_ans}")
                    pass
                except Exception as e:
                    print(e)
        else:
            self.client.send_message(f"ER Formát čísla účtu není správný.")


    def account_remove(self, accountdata):
        try:
            account_number, ip_address = accountdata.split('/')
            if (int(account_number) >= 10000 and int(account_number) <= 99999) :
                if re.fullmatch(str(self.ip), str(ip_address)):
                    all_accounts = self.account_Dao.select_all()
                    found = 0
                    for account in all_accounts:
                        if re.fullmatch(str(account_number),str(account.account_number)) and account.currency == 0:
                            found += 1
                            self.account_Dao.delete(account_number)
                            return self.client.send_message(f"AR")
                    if found == 0:
                        self.client.send_message(f"ER číslo bankovního účtu a částka není ve správném formátu.")
            else:
                self.client.send_message(f"ER číslo bankovního účtu a částka není ve správném formátu.")
        except Exception as e:
            print(e)


    def bank_amount(self):
        try:
            all_accounts = self.account_Dao.select_all()
            suma = 0
            for account in all_accounts:
                suma += account.currency
            return self.client.send_message(f"BA {suma}")
        except Exception:
            self.client.send_message(f"ER aktuálně nebylo možné vypsat celou finanční sumu.")



    def number_of_clients(self):
        try:
            all_accounts = self.account_Dao.select_all()
            sum_of_clients = 0
            for account in all_accounts:
                sum_of_clients += 1
            return self.client.send_message(f"BN {sum_of_clients}")
        except Exception:
            self.client.send_message(f"ER aktuálně nebylo možné vypsat celou finanční sumu.")

    def command_redirection(self, redirected_command):
        functional_port = None
        try:
            split_data = redirected_command.split(' ')
            account_number, ip_address = split_data[1].split('/')
            for port in range(65525,65536):
                try:
                    server_inet_address = (ip_address, port)
                    bank_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    bank_socket.settimeout(0.2)
                    bank_socket.connect(server_inet_address)
                    functional_port = port
                    bank_socket.close()
                    break
                except socket.error:
                    pass
            else:
                sorry = f"Tento bankovní kod nebyl nalezen"
                return sorry
        except Exception:
            return None
        else:
            try:
                server_inet_address = (ip_address, functional_port)
                bank_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                bank_socket.connect(server_inet_address)
                command = f"{redirected_command}\r\n"
                bank_socket.sendall(command.encode("utf-8"))
                response = bank_socket.recv(4096).decode("utf-8").strip()
                bank_socket.close()
                return response
            except Exception as e:
                print(e)
