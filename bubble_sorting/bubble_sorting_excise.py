list_of_ages = [8,4,5,18,0]

def print_backwards(list_of_ages):
    new = []
    count = len(list_of_ages) -1
    for index in range(0,len(list_of_ages)):
        new.append(list_of_ages[count])
        count -=1
        print(new) 


print_backwards(list_of_ages)

def bubble_sort(list_of_ages):
    for index in range(0,len(list_of_ages)):
        for follow_up_index in range(0,len(list_of_ages)):
            if list_of_ages[index] < list_of_ages[follow_up_index]:
                number = list_of_ages[index]
                list_of_ages[index] = list_of_ages[follow_up_index]
                list_of_ages[follow_up_index] = number
    print(list_of_ages)

    
bubble_sort(list_of_ages)                  
                       
