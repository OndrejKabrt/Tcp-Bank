import random
import re

from Account import Account
from AccountDAO import AccountDAO


class Applications():

    def __init__(self, client):
        self.client = client
        self.account_Dao = AccountDAO()
        self.ip = str(self.client.connection).split("laddr=('")[1].split("',")[0]


    ##Todo Metoda na přesměrování příkazu na jinou ip addresu

    def account_create(self, accountdata = None):
        try:
            if(accountdata):
                raise Exception
            all_accounts = self.account_Dao.select_all()
            if not all_accounts:
                all_accounts = []
            new_account = random.choice([i for i in range(10000, 99999) if i not in all_accounts])
        except Exception as e:
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
                #else:
                    #Ta metoda na presmerovani
                    #pass
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
            #else:
                #Ta metoda na presmerovani
                #pass
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
                        return self.client.send_message(f"AB {balance}")
            #else:
            #Ta metoda na presmerovani
            #pass
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
                #else:
                    #Ta metoda na presmerovani
                    #pass
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
        except Exception as e:
            self.client.send_message(f"ER aktuálně nebylo možné vypsat celou finanční sumu.")



    def number_of_clients(self):
        try:
            all_accounts = self.account_Dao.select_all()
            sum_of_clients = 0
            for account in all_accounts:
                sum_of_clients += 1
            return self.client.send_message(f"BN {sum_of_clients}")
        except Exception as e:
            self.client.send_message(f"ER aktuálně nebylo možné vypsat celou finanční sumu.")