import mysql.connector
import re

class CommonFunction:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'db_password',
            database = 'db_name'
        )
        self.mycursor = self.mydb.cursor()
    
    def _verify_pwd_cpwd(self):
        while True:
            self.pwd = input('Password : ')
            if (self.verify_pwd(self.pwd)): 
                while True:
                    self.cpwd = input('Confirm Password :')
                    if self.pwd == self.cpwd:
                        return True    
                    else:
                        print("Password mismatch")

    def verify_pwd(self,pwd):
        SpecialSym =['$', '@', '#', '%','!','&'] 
        val = True
        
        if len(self.pwd) < 8: 
            print('Password must contain at least eight characters') 
            val = False     
        if len(self.pwd) > 20: 
            print('Password must not be greater eight characters') 
            val = False
        if not any(char.isdigit() for char in self.pwd): 
            print('Password must contain at least one number (0-9)') 
            val = False
        if not any(char.isupper() for char in self.pwd): 
            print('Password must contain at least one uppercase letter (a-z)') 
            val = False
        if not any(char.islower() for char in self.pwd): 
            print('Password must contain at least one lowercase letter (a-z)') 
            val = False
        if not any(char in SpecialSym for char in self.pwd): 
            print('Password must contain at least one of the symbols $@#%!&') 
            val = False
        if val: 
            return val 

    def _verify_email(self):
        while True:
            self.email = input("Email :")
            check = re.findall("([a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[.com]+)", self.email)
            if self.email in check:
                return True

    def get_email(self):
        return self.email 
    
    def get_pwd(self):
        return self.pwd

