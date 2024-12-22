n=int(input("How many characters will you choose for the password = "))
print("\nFor password you can use:")
print("\n**Upper case letter(A to Z)**")
print("\n**Lower case letter(a to z)**")
print("\n**Digits(0 to 9)**")
print("\n**If you want more security, you can also use special symbols(!,@,#.$.%,&,*,etc)**")

def create_pass():
    while True:
        password = input("\nEnter your password: ")
        confirm = input("\nRe-enter password to confirm: ")
        
        if password == confirm:
            
            print(password, "\nsaved successfully.")
            return password
           
        else:
            print("\nPasswords do not match. Please try again.")


def valid_pass(saved_pass):
    while True:
        validation = input("\nFor validation enter your confirmed password: ")
    
        if validation == saved_pass:
            print("\nPassword matches.")
            break
        
        elif validation != saved_pass:
            print("Wrong")
            print("\n1 for try again")
            print("\n2 for reset password")
            choice = input("\nchoose 1/2:")
            if choice== "1":
                continue
            elif choice =="2":
                return create_pass()
                continue
            else:
                print("\nChoose valid choice.")
                
        
saved_pass=create_pass()
valid_pass(saved_pass)




