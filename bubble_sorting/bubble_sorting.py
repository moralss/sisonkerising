
def bubble_sorting(list_ages,total_number_of_ages):
    if total_number_of_ages == 0:
        print(list_ages)
        return
        


    if (len(list_ages) == 1):
        print(list_ages)
        return
        
    else:
        for index in range(0,total_number_of_ages):
            if(list_ages[index] > list_ages[index+1]):
                list_ages[index],list_ages[index+1] = list_ages[index+1],list_ages[index]
            
#        bubble_sorting(list_ages,total_number_of_ages-1)

list_ages=[8,4,5,18,0]

bubble_sorting(list_ages,len(list_ages)-1)
        
