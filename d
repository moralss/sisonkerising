[1mdiff --git a/README (2).md b/README (2).md[m
[1mdeleted file mode 100644[m
[1mindex ce11948..0000000[m
[1m--- a/README (2).md[m	
[1m+++ /dev/null[m
[36m@@ -1,12 +0,0 @@[m
[31m-# Clash-of-the-titans[m
[31m-[m
[31m-I couldn’t have done it without help from the following people.[m
[31m-[m
[31m-Bucky Roberts[m
[31m-[m
[31m-Justin Armstrong[m
[31m-[m
[31m-Thank you for helping me.[m
[31m-[m
[31m-I got help from the following site[m
[31m-Stock over flow [m
[1mdiff --git a/README (3).md b/README (3).md[m
[1mdeleted file mode 100644[m
[1mindex f7bbcde..0000000[m
[1m--- a/README (3).md[m	
[1m+++ /dev/null[m
[36m@@ -1 +0,0 @@[m
[31m-# banking_app[m
\ No newline at end of file[m
[1mdiff --git a/README.md b/README.md[m
[1mdeleted file mode 100644[m
[1mindex e8ef821..0000000[m
[1m--- a/README.md[m
[1m+++ /dev/null[m
[36m@@ -1,24 +0,0 @@[m
[31m-[m
[31m-$ git remote add origin https://github.com/moralss/sisonkerising.git[m
[31m-[m
[31m-user@PlayOnSports MINGW32 ~ (master)[m
[31m-$ git init[m
[31m-Reinitialized existing Git repository in C:/Users/user/.git/[m
[31m-[m
[31m-user@PlayOnSports MINGW32 ~ (master)[m
[31m-$ git add README.md[m
[31m-fatal: pathspec 'README.md' did not match any files[m
[31m-[m
[31m-user@PlayOnSports MINGW32 ~ (master)[m
[31m-$ git status[m
[31m-On branch master[m
[31m-[m
[31m-$ git status[m
[31m-On branch master[m
[31m-[m
[31m-Initial commit[m
[31m-[m
[31m-Untracked files:[m
[31m-  (use "git add <file>..." to include in what will be committed)[m
[31m-[m
[31m-        README.md.txt[m
[1mdiff --git a/banking/README (2).md b/banking/README (2).md[m
[1mnew file mode 100644[m
[1mindex 0000000..ce11948[m
[1m--- /dev/null[m
[1m+++ b/banking/README (2).md[m	
[36m@@ -0,0 +1,12 @@[m
[32m+[m[32m# Clash-of-the-titans[m
[32m+[m
[32m+[m[32mI couldn’t have done it without help from the following people.[m
[32m+[m
[32m+[m[32mBucky Roberts[m
[32m+[m
[32m+[m[32mJustin Armstrong[m
[32m+[m
[32m+[m[32mThank you for helping me.[m
[32m+[m
[32m+[m[32mI got help from the following site[m
[32m+[m[32mStock over flow[m[41m [m
[1mdiff --git a/banking/banking_app.py b/banking/banking_app.py[m
[1mnew file mode 100644[m
[1mindex 0000000..ef4dd69[m
[1m--- /dev/null[m
[1m+++ b/banking/banking_app.py[m
[36m@@ -0,0 +1,67 @@[m
[32m+[m[32m#sisonke rising[m
[32m+[m[32mimport random[m
[32m+[m[32mimport os[m[41m [m
[32m+[m[32maccount_number = random.randint(1,10000000000)[m[41m   [m
[32m+[m[32mprint("join mobank today the new way to banking  %s" %os.getlogin())[m
[32m+[m
[32m+[m
[32m+[m[41m    [m
[32m+[m[32mdef create_login_profile():[m
[32m+[m[41m    [m
[32m+[m[32m    global user_name,surname[m
[32m+[m[32m    user_name = input("create a user name: ")[m
[32m+[m[32m    name = input("type your name: ")[m
[32m+[m[32m    surname = input("type your surname: ")[m
[32m+[m[32m    new_password = (input("Please enter a password that consists out of 6 digits: "))[m
[32m+[m[41m    [m
[32m+[m[32m    while len(new_password) < 6 :[m
[32m+[m[32m        print("Your password length should be greater than 6")[m
[32m+[m[32m        new_password = input("Please enter your new password")[m
[32m+[m[41m        [m
[32m+[m[32m    if len(new_password) > 6:[m
[32m+[m[41m        [m
[32m+[m[32m        print("YOUR NAME IS %s \nYOUR SURNAME IS %s \nYOUR USER NAME IS %s \nYOUR PASSWORD IS %s" %(name,surname,user_name,new_password))[m
[32m+[m[32m        confirm = input('type yes to confirm :')[m
[32m+[m[41m            [m
[32m+[m[32m        if confirm == 'yes':[m
[32m+[m[41m            [m
[32m+[m[32m            print("you are done applying at mobank : ")[m
[32m+[m[32m            print("your acount number is %s" % ( account_number))[m
[32m+[m[32m            print("")[m
[32m+[m[32m            print("%s %s to deposit money type deposit(amount) to withdraw money type with_draw(amount) to check balance type check_bank_balance()" %(name,surname))[m
[32m+[m[41m            [m
[32m+[m[32m        else:[m
[32m+[m[32m            print("failed to comfirm accept")[m
[32m+[m[41m            [m
[32m+[m[41m            [m
[32m+[m[41m            [m
[32m+[m[41m    [m
[32m+[m[32mcreate_login_profile()[m
[32m+[m
[32m+[m[32mfirst_amount = [][m
[32m+[m
[32m+[m[41m           [m
[32m+[m[32mdef deposit(diposit_amount):[m
[32m+[m[32m   first_amount.append(diposit_amount)[m
[32m+[m[32m   total_diposit = (sum(first_amount))[m
[32m+[m[32m   print("%s you just diposited R%s into you account"%(user_name,diposit_amount))[m
[32m+[m[32m   print("%s you have R%s in your account " %(user_name ,total_diposit))[m
[32m+[m
[32m+[m
[32m+[m[32mdef with_draw(amount):[m
[32m+[m[41m    [m
[32m+[m[32m    first_amount.append(-amount)[m
[32m+[m[32m    total_with_drawen = (sum(first_amount))[m
[32m+[m[32m    print("%s you have Withdrawn R%s" %(user_name,amount))[m[41m [m
[32m+[m[32m    if total_with_drawen < 0:[m[41m [m
[32m+[m[32m        print(" %s you  have no money in your account to Withdrawn don't amount "%(user_name))[m
[32m+[m[41m          [m
[32m+[m[32m    elif total_with_drawen > 0:[m
[32m+[m[32m        print("%s you have R%s left in your amount "%(user_name ,total_with_drawen))[m
[32m+[m[41m            [m
[32m+[m[41m    [m
[32m+[m[32mdef check_bank_balance():[m
[32m+[m[32m    balance = (sum(first_amount))[m
[32m+[m[32m    print("%s you have R%s in your account "%(user_name,balance))[m
[32m+[m[41m    [m
[32m+[m
[1mdiff --git a/banking_app.py b/banking_app.py[m
[1mdeleted file mode 100644[m
[1mindex ef4dd69..0000000[m
[1m--- a/banking_app.py[m
[1m+++ /dev/null[m
[36m@@ -1,67 +0,0 @@[m
[31m-#sisonke rising[m
[31m-import random[m
[31m-import os [m
[31m-account_number = random.randint(1,10000000000)   [m
[31m-print("join mobank today the new way to banking  %s" %os.getlogin())[m
[31m-[m
[31m-[m
[31m-    [m
[31m-def create_login_profile():[m
[31m-    [m
[31m-    global user_name,surname[m
[31m-    user_name = input("create a user name: ")[m
[31m-    name = input("type your name: ")[m
[31m-    surname = input("type your surname: ")[m
[31m-    new_password = (input("Please enter a password that consists out of 6 digits: "))[m
[31m-    [m
[31m-    while len(new_password) < 6 :[m
[31m-        print("Your password length should be greater than 6")[m
[31m-        new_password = input("Please enter your new password")[m
[31m-        [m
[31m-    if len(new_password) > 6:[m
[31m-        [m
[31m-        print("YOUR NAME IS %s \nYOUR SURNAME IS %s \nYOUR USER NAME IS %s \nYOUR PASSWORD IS %s" %(name,surname,user_name,new_password))[m
[31m-        confirm = input('type yes to confirm :')[m
[31m-            [m
[31m-        if confirm == 'yes':[m
[31m-            [m
[31m-            print("you are done applying at mobank : ")[m
[31m-            print("your acount number is %s" % ( account_number))[m
[31m-            print("")[m
[31m-            print("%s %s to deposit money type deposit(amount) to withdraw money type with_draw(amount) to check balance type check_bank_balance()" %(name,surname))[m
[31m-            [m
[31m-        else:[m
[31m-            print("failed to comfirm accept")[m
[31m-            [m
[31m-            [m
[31m-            [m
[31m-    [m
[31m-create_login_profile()[m
[31m-[m
[31m-first_amount = [][m
[31m-[m
[31m-           [m
[31m-def deposit(diposit_amount):[m
[31m-   first_amount.append(diposit_amount)[m
[31m-   total_diposit = (sum(first_amount))[m
[31m-   print("%s you just diposited R%s into you account"%(user_name,diposit_amount))[m
[31m-   print("%s you have R%s in your account " %(user_name ,total_diposit))[m
[31m-[m
[31m-[m
[31m-def with_draw(amount):[m
[31m-    [m
[31m-    first_amount.append(-amount)[m
[31m-    total_with_drawen = (sum(first_amount))[m
[31m-    print("%s you have W