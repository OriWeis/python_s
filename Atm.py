'''Ori Weis'''
'''29.4.21'''
'''Class Of Atm For Clients'''
'''Interpeter 3.8'''
import socket
import random
import sqlite3

con = sqlite3.connect('mydb.db')
cur = con.cursor()

class Atm:

    def __init__(self):
        data_to_bank=""
        self.my_socket = socket.socket()
        self.my_socket.connect(('127.0.0.1', 1801)) #connects to loopback address on port 1801 because i worked with 1 pc
        while True:
            try:
                # sending the code the the server
                code=input("Welcome to Ori's Bank!\nLogin = 1 Create new account = 2: ")
                if code=='1':
                    self.my_socket.send(bytes((code).encode()))
                    break
                elif code=='2':
                    # creating new account
                    self.my_socket.send(bytes((code).encode()))
                    while True:
                        # generating a random 6 digit number and checks if its available
                        account_number = random.randint(100000, 999999)
                        result = cur.execute("SELECT account_number FROM Bank WHERE account_number=?",
                                             (account_number,)).fetchone()
                        if result: # if not available, generate again
                            continue
                        break
                    self.my_socket.send(bytes((str(account_number)).encode())) # sending the account number to the server
                    print("Your account number is: %d" % account_number)
                    name = input("Enter the account owner name: ")
                    self.my_socket.send(bytes((name).encode())) # sending the account name to the server
                    while True:
                        # asking for a PIN code. if its not 4 digits long, ask for another one
                        pin = input("Enter PIN code (must be 4 digits only): ")
                        if len(pin) != 4:
                            print("Incorrect PIN!\n")
                        else:
                            try:
                                # checking if the PIN is consisted of digits only
                                check = int(pin)
                                if check < 0:
                                    print("Incorrect PIN!\n")
                                else:
                                    break
                            except:
                                print("Incorrect PIN!\n")
                    self.my_socket.send(bytes((pin).encode())) # sending the pin code to the server
                    while True:
                        balance = input("Enter the amount of money you would like to deposit: ")
                        try:
                            if int(balance) <= 0:
                                print("Error! Must deposit positive amount!")
                            else:
                                break
                        except:
                            print("Incorrect amount!\n")
                    self.my_socket.send(bytes((balance).encode())) # sending the starting balance to the server
                    print("New bank account has been created successfully!")
                else:
                    print("Wrong input! Please try again")
            except:
                print("Wrong input! Please try again")

        while True:
            acc = input("Enter your account number: ")
            pin = input("Enter your PIN: ")
            self.my_socket.send(bytes((acc).encode()))
            self.my_socket.send(bytes((pin).encode()))
            from_bank = self.my_socket.recv(1024).decode()
            if from_bank == "True":
                while str(data_to_bank) != "4":
                    from_bank = self.my_socket.recv(1024).decode()
                    print(from_bank)
                    data_to_bank = input("")
                    self.my_socket.send(bytes((data_to_bank).encode()))
                    if data_to_bank=='1':
                        amount=self.check_amount(1)
                        self.my_socket.send(bytes(str(amount).encode()))
                        if amount!=-1:
                            print(self.my_socket.recv(1024).decode())
                    elif data_to_bank=='2':
                        amount = self.check_amount(2)
                        self.my_socket.send(bytes(str(amount).encode()))
                        if amount != -1:
                            print(self.my_socket.recv(1024).decode())
                    elif data_to_bank=='3':
                        print(self.my_socket.recv(1024).decode())
                    elif data_to_bank!='4':
                        print("Incorrect code entered! Please try again")
                break
            else:
                print("Incorrect credentials! Please try again")
        self.my_socket.close()

    def check_amount(self, flag):
        try:
            if flag==1:
                amount = int(input("Enter amount to deposit in your account: "))
            else:
                amount = int(input("Enter amount to withdraw from your account: "))
            if amount <= 0:
                print("Error! Must deposit positive amount!")
            else:
                return amount
        except:
            print("Incorrect amount!\n")
        return -1


def main():
    atm=Atm()

main()
