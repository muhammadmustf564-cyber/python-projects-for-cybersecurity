def pass_check():
    for x in range(3):

        # take username and password from user
        username = input("Enter username:")
        password = input("Enter password:")

        if username == 'admin' and password == '123456':
            result = "Access Granted"
            return result
        else:
            print("Wrong attempt")

            # if user entered the wrong username and password in 3rd attempt
            if x == 2:
                return "Account Locked"
        
print(pass_check())