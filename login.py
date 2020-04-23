import mysql.connector
import getpass
import re
import numpy
from call import CommonFunction

class Login(CommonFunction):
    def __init__(self):
        CommonFunction.__init__(self)
        self.logic()
        self.login_db()  

    def update(self):
        self.mycursor.execute('Select phone,email FROM register') #register is the table name in the database
        myresult = self.mycursor.fetchall()
        for db_phone,db_email in myresult:
            if self.luser == db_phone:
                CommonFunction._verify_pwd_cpwd(self)
                self.mycursor.execute("UPDATE register SET pwd = %s WHERE phone=%s ",(CommonFunction.get_pwd(self),self.luser))
            elif self.luser == db_email:
                CommonFunction._verify_pwd_cpwd(self)
                self.mycursor.execute("UPDATE register SET pwd = %s WHERE email=%s ",(CommonFunction.get_pwd(self),CommonFunction.get_email(self)))
        self.mydb.commit()
        print('Updated successfully')

    def logic(self):
        getinput = True
        while True:
            while(getinput == True):
                print('Select Action \n 1.Email \n 2.Phone')
                user_choice = input()
                if user_choice == '1':
                    CommonFunction._verify_email(self)
                    self.lpwd = input('Password :')
                    self.luser = str(numpy.char.lower(CommonFunction.get_email(self)))
                    getinput = False
                elif user_choice == '2':
                    self.phone = int(input('Phone :'))
                    self.lpwd = input('Password :')
                    self.luser = self.phone
                    getinput = False
                else:
                    print("Please enter valid input")
            #check whether name or password is blank or not
            if (self.luser != "" and self.lpwd != ""):
                return True     
   
    def retry_pwd(self):
        self.mycursor.execute('Select phone,email FROM register')
        myresult = self.mycursor.fetchall()
        for db_phone,db_email in myresult:
            if self.luser == db_phone:
                data = self.luser
                self.mycursor.execute("Select email FROM register where phone = %s" , (data,))
                query =  self.mycursor.fetchall()
                self.email = query            
            elif self.luser == db_email:
                self.email = CommonFunction.get_email(self)
        self.lpwd = input('Password :')
        self.login_db()

    def login_db(self):
        self.mycursor.execute('Select phone,email,pwd FROM register')
        myresult = self.mycursor.fetchall()
        temp = False
        
        for db_phone,db_email,db_pwd in myresult:
            if (self.luser == db_phone  or self.luser == db_email) and self.lpwd == db_pwd:
                print('Login successful')
                temp = True
                # break
            elif(self.luser == db_phone  or self.luser == db_email) and self.lpwd != db_pwd:
                print('Invalid password')
                pwd_input = True
                while (pwd_input == True):
                    print('Select Action \n 1.Forget Password? -->Update password \n 2.Retry \n 3.Exit')
                    user_choice = input()
                    if user_choice == '1':
                        self.update()
                        pwd_input = False
                        temp = True
                    elif user_choice == '2':
                        self.retry_pwd()
                        pwd_input = False
                        temp = True
                    elif user_choice == '3':
                        pwd_input = False
                        temp = True
                        # break
                    else:
                        print("Please enter valid input")
            
        if temp == False:          
            print("No user found. Redirecting you to register")
            print('****************************************')
            from registration import Registration
l = Login()

