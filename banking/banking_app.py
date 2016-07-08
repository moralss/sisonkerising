#sisonke rising
import random
import os 
account_number = random.randint(1,10000000000)   
print("join mobank today the new way to banking  %s" %os.getlogin())


    
def create_login_profile():
    
    global user_name,surname
    user_name = input("create a user name: ")
    name = input("type your name: ")
    surname = input("type your surname: ")
    new_password = (input("Please enter a password that consists out of 6 digits: "))
    
    while len(new_password) < 6 :
        print("Your password length should be greater than 6")
        new_password = input("Please enter your new password")
        
    if len(new_password) > 6:
        
        print("YOUR NAME IS %s \nYOUR SURNAME IS %s \nYOUR USER NAME IS %s \nYOUR PASSWORD IS %s" %(name,surname,user_name,new_password))
        confirm = input('type yes to confirm :')
            
        if confirm == 'yes':
            
            print("you are done applying at mobank : ")
            print("your acount number is %s" % ( account_number))
            print("")
            print("%s %s to deposit money type deposit(amount) to withdraw money type with_draw(amount) to check balance type check_bank_balance()" %(name,surname))
            
        else:
            print("failed to comfirm accept")
            
            
            
    
create_login_profile()

first_amount = []

           
def deposit(diposit_amount):
   first_amount.append(diposit_amount)
   total_diposit = (sum(first_amount))
   print("%s you just diposited R%s into you account"%(user_name,diposit_amount))
   print("%s you have R%s in your account " %(user_name ,total_diposit))


def with_draw(amount):
    
    first_amount.append(-amount)
    total_with_drawen = (sum(first_amount))
    print("%s you have Withdrawn R%s" %(user_name,amount)) 
    if total_with_drawen < 0: 
        print(" %s you  have no money in your account to Withdrawn don't amount "%(user_name))
          
    elif total_with_drawen > 0:
        print("%s you have R%s left in your amount "%(user_name ,total_with_drawen))
            
    
def check_bank_balance():
    balance = (sum(first_amount))
    print("%s you have R%s in your account "%(user_name,balance))
    

