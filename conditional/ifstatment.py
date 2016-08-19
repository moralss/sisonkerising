count = 6
while count > 1:
    age = int(input('how old are you? :'))
    
    if age > 20:
        print("You are too old")
    elif age == 20:
        print("you are equal to 20")
    else:
        print("you are too small")
        
    count -=1
