import getpass
import re
import sys
import mysql.connector
import numpy
from call import CommonFunction


class Registration(CommonFunction):
    def __init__(self):
        CommonFunction.__init__(self)
        self.verify_name()
        self.verify_phone()
        CommonFunction._verify_email(self)
        CommonFunction._verify_pwd_cpwd(self)
        self.db()

    def verify_name(self):
        # getuser()
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:1234567890]')
        while True:
            self.name = input("Full Name :")
            if (regex.search(self.name) == None):
                if len(self.name) > 5:
                    return True
                else:
                    print('Minimum length must be 6')
            else:
                print("Special characters/numbers are not allowed")

    def verify_phone(self):
        while True:
            self.phone = int(input("Phone number :"))
            list_phone = []
            for number in str(self.phone):
                list_phone.append(number)
            if ((len(list_phone) == 10) and (list_phone[0] == '9' or list_phone[0] == '8' or list_phone[0] == '7')):
                return True
            else:
                print("Invalid phone number")

    def db(self):
        self.mycursor.execute('Select email,phone FROM register')
        myresult = self.mycursor.fetchall()
        temp = False
        update_name = str(numpy.char.capitalize(self.name))
        update_email = str(numpy.char.lower(self.email))
        for db_email, db_phone in myresult:
            if (self.email == db_email or self.phone == db_phone):
                print("User exist. Redirectly you to login")
                print('***********************************')
                from login import Login
                temp = True
                break
        if temp == False:
            self.mycursor.execute("INSERT INTO register (name,phone,email,pwd) VALUES (%s,%s,%s,%s)", (
                update_name, self.phone, update_email, self.pwd))
            self.mydb.commit()
            print("Registeration successfully")


user = Registration()
