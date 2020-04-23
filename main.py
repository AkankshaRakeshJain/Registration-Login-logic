# sudo python3 -m pip install numpy
def call_registration():
    print('Registration Page')
    from registration import Registration


def call_login():
    print("Login Page")
    from login import Login


# main
getinput = True
len = 4
if __name__ == "__main__":
    while (getinput == True):
        print('Select Action \n 1.Register \n 2.Login \n 3.Exit')
        user_choice = input()
        if user_choice == '1':
            call_registration()

            getinput = False
        elif user_choice == '2':
            call_login()

            getinput = False
        elif user_choice == '3':
            print('Exit')
            getinput = False
        else:
            print("Please enter valid input. ")
            len -= 1
            if len == 0:
                getinput = False
