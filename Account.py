class Account:
    def __init__(self, account_number, currency):
        if not isinstance(int(account_number), int):
            raise TypeError("account_number must be an integer")
        self.account_number = account_number

        if not isinstance(int(currency), int):
            raise TypeError("currency must be an integer")
        self.currency = currency

    def __str__(self):
        return (f"Account number: {self.account_number}, Currency {self.currency} ")
