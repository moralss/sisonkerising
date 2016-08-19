my_list_1 = [1,5,8,11,12,15]

def get_value_at( index , my_list):
    show_index = my_list[index]
    return(show_index)


result_for_value = get_value_at(1,my_list_1)
print(result_for_value)

    
def get_index_at( value , my_list):
    length_of_list = range(0,len(my_list)-1) 
    for index in length_of_list:
        if my_list[index] == value:
            return index


             
result_for_index = get_index_at(1,my_list_1)
print(result_for_index)



def sisonke_length(my_list):
    current_total = 0
    for index in my_list:
        current_total = current_total + 1
    return(current_total)



result_for_length = sisonke_length(my_list_1)
print(result_for_length)



