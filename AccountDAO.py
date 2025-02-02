from DatabaseSingleton import *
from Account import Account

class AccountDAO:

    def save(self,a):
        sql = "INSERT  INTO account (account_number, currency) values (%s, %s);"
        val = [a.account_number, a.currency]
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            cursor.execute("START TRANSACTION;")
            cursor.execute(sql, val)
        except Exception as e:
            print("7")
            print(e)
            cursor.execute("ROLLBACK;")
        else:
            cursor.execute("COMMIT;")
        finally:
            conn.close()


    def update_positive(self, a):
        sql = "UPDATE account SET currency = currency + %s WHERE account_number = %s;"
        val = [a.currency, a.account_number]
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            cursor.execute("START TRANSACTION;")
            cursor.execute(sql, val)
        except Exception as e:
            print(e)
            cursor.execute("ROLLBACK;")
        else:
            cursor.execute("COMMIT;")
        finally:
            conn.close()

    def update_negative(self, a):
        sql = "UPDATE account SET currency = currency - %s WHERE account_number = %s;"
        val = [a.currency, a.account_number]
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            cursor.execute("START TRANSACTION;")
            cursor.execute(sql, val)
        except Exception as e:
            print(e)
            cursor.execute("ROLLBACK;")
        else:
            cursor.execute("COMMIT;")
        finally:
            conn.close()


    def delete(self,account_number):
        sql = "DELETE FROM account WHERE account_number = %s;"
        val = [account_number]
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            cursor.execute("START TRANSACTION;")
            cursor.execute(sql, val)
        except Exception as e:
            print(e)
            cursor.execute("ROLLBACK;")
        else:
            cursor.execute("COMMIT;")
        finally:
            conn.close()


    def select_balance(self,account_number):
        sql = "SELECT currency FROM account WHERE account_number = %s;"
        val = [account_number]
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            cursor.execute(sql, val)
            result = cursor.fetchall()
        except Exception as e:
            print(e)

        else:
            cursor.execute("COMMIT;")
        finally:
            conn.close()
            return result


    def select_all(self):
        sql = "SELECT * FROM account;"
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except Exception as e:
            print(e)
        else:
            balances = []
            for row in result:
                a = Account(row[0], row[1])
                balances.append(a)
        finally:
            conn.close()
            if(len(balances) > 0):
                return balances

    def client_count(self):
        sql = "SELECT COUNT(*) FROM account;"
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            conn.close()
            return result