from lib.social_network import *

class AccountRepository:
    def __init__(self,connection):
        self.connection = connection 

    def all(self):
        rows = self.connection.execute('SELECT * FROM accounts')
        accounts = []
        for row in rows:
            account = Account (
                row["id"],
                row["email"],
                row["username"])
            accounts.append(account)
        return accounts
    
    def find(self, account_id):
        rows = self.connection.execute('SELECT * FROM accounts WHERE id = %s', [account_id])
        row = rows[0]
        return Account(
                row["id"],
                row["email"],
                row["username"])
    
    # def get_post_counts(self):
    #     pass

    def create(self,account):
        self.connection.execute('INSERT INTO accounts (email, username) VALUES (%s, %s)', [account.email, account.username])
        return None
        pass
    
    def delete(self,account_id):
        self.connection.execute('DELETE FROM accounts WHERE id = %s', [account_id])
        return None