def fibonacci(fibonacci_range):
    if fibonacci_range == 1 or fibonacci_range ==2:
        return 1
    show = fibonacci(fibonacci_range-1) + fibonacci(fibonacci_range-2)
    return show
    

def show_histogram(end):
    for i in range(1,end):
        print(fibonacci(i) * "*" )
    
show_histogram(13)



    
    

