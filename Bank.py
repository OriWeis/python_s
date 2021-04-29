''' Ori Weis '''
'''29.4.21'''
'''This Bank Class Will Be The Server'''
'''Interpeter 3.8'''
import sqlite3
import socket

con = sqlite3.connect('mydb.db')
cur = con.cursor()

class Bank:


    def __init__(self, fortune, accounts):
        self.fortune=fortune
        self.accounts=accounts

    #adding Account To The DB
    def add_account(self, account_num, name, pin, balance):
        cur.execute("INSERT INTO Bank (account_number, name, pin, balance) VALUES(?,?,?,?)"
                       ,(account_num, name, pin, balance))
        con.commit()
        print("New bank account has been created successfully!")

    def deposit(self, account_num, amount):
        m="Success! account have deposited %d$." %amount
        result = cur.execute("SELECT * FROM Bank WHERE account_number=?", (account_num, )).fetchone()
        cur.execute("UPDATE Bank SET balance=? WHERE account_number=?", (result[3]+amount, account_num))
        con.commit()
        print(m)
        return m

    def withdraw(self, account_num, amount):
        m = "Error Occured!"
        result = cur.execute("SELECT * FROM Bank WHERE account_number=?", (account_num, )).fetchone()
        if amount > result[3]:
            m = ("Cant withdraw more than %d$!" %result[3])
        else:
            cur.execute("UPDATE Bank SET balance=? WHERE account_number=?", (result[3] - amount, account_num))
            con.commit()
            m = "Success! account have withdraw %d$." % amount
        print(m)
        return m

    def check_credentials(self, acc, pin_code):
        result = cur.execute("SELECT * FROM Bank WHERE account_number=? AND pin=?", (acc, pin_code)).fetchone()
        if result:
            return True
        return False

    def check_balance(self, account_num):
        result = cur.execute("SELECT * FROM Bank WHERE account_number=?", (account_num,)).fetchone()
        m = ("You have %d$ in your account" % result[3])
        print(m)
        return m


'''Main function That handles The Client Server Connection'''
def main():
    sum=0
    count=0
    action='0'
    msg = '''\nWelcome to the Ori's Bank!
Enter the code of the action you would like to execute:
1 = deposit
2 = withdraw
3 = check balance
4 = exit\n
The code: '''
    server_socket=socket.socket()
    server_socket.bind(('0.0.0.0',1801))
    server_socket.listen(5)
    (client_socket, client_address) = server_socket.accept()
    print("Client has entered")
    print("All of the bank accounts:\n"
          "account_num | name | PIN | balance\n"
          "___________________________________")
    rows = cur.execute("SELECT * FROM Bank").fetchall()
    if rows:
        for row in rows:
            print(row)
            count+=1
            sum+=row[3]
    else:
        print("No bank accounts at the moment...")
    my_bank = Bank(sum, count)
    while True and action!='4':
        first_code = int(client_socket.recv(1024).decode())
        print("The code is: %d" %first_code)
        while True:
            if first_code==1:
                acc = client_socket.recv(1024).decode()
                print(acc)
                pin_code = client_socket.recv(1024).decode()
                print(pin_code)
                credentials = my_bank.check_credentials(acc, pin_code)
                print(credentials)
                client_socket.send(bytes((str(credentials)).encode('utf-8')))
                if credentials == True:
                    while action != '4':
                        client_socket.send(bytes((msg).encode('utf-8')))
                        action = client_socket.recv(1024).decode()
                        if action == '1':
                            amount = client_socket.recv(1024).decode()
                            if int(amount) > 0:
                                client_socket.send(bytes(my_bank.deposit(acc, int(amount)).encode('utf-8')))
                            else:
                                client_socket.send(bytes((msg).encode('utf-8')))
                        elif action=='2':
                            amount = client_socket.recv(1024).decode()
                            if int(amount) > 0:
                                client_socket.send(bytes(my_bank.withdraw(acc, int(amount)).encode('utf-8')))
                            else:
                                client_socket.send(bytes((msg).encode('utf-8')))
                        elif action == '3':
                            client_socket.send(bytes(my_bank.check_balance(acc).encode('utf-8')))
                        elif action=='4':
                            print("Goodbye!")
                            break
                        else:
                            print("Invalid input!")
                            client_socket.send(bytes((msg).encode('utf-8')))
                    break
            else:
                print("Creating new account...")
                acc_num = int(client_socket.recv(1024).decode())
                print(acc_num)
                name = client_socket.recv(1024).decode()
                print(name)
                pin = client_socket.recv(1024).decode()
                print(pin)
                balance = client_socket.recv(1024).decode()
                print(balance)
                my_bank.add_account(acc_num, name, pin, balance)
                first_code = int(client_socket.recv(1024).decode())
                print("The code is: %d" % first_code)
    server_socket.close()

if __name__ == '__main__':
    main()
