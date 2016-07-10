favourite_cars = {1:'benz',2:'audi',3:'golf'}

#It print underneath each other 
def display_cars():
    for position in favourite_cars:
        print("%s %s" %(position , favourite_cars[position]))

display_cars()
