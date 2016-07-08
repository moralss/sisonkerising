brown_bread_costs = 10.50
soda_costs = 7.40
brown_sugar_costs = 5.40


current_stock = {"brown_bread":2,"brown_sugar":3,"soda":2}

def calculate_total_stock(new_stock):
    total_of_stock = list(new_stock.values()) + list(current_stock.values())
    sum_of_stock = sum(total_of_stock)
    
    
    for key in current_stock:
        if current_stock[key] == new_stock[key]:
            total_amount_of_stock = current_stock[key] + new_stock[key]
            print("for %s you have a total of %s" % (key ,total_amount_of_stock))
            print("")
    print("total amount of products %s" %( sum_of_stock))       

            

def calculate_price_new_stock(items):
    price_of_the_total_amount_of_brown_bread = items["brown_bread"] * float(brown_bread_costs)
    price_of_the_total_amount_of_brown_sugar = items["brown_sugar"] * float(brown_sugar_costs)
    price_of_the_total_amount_of_soda = items["soda"] * float(soda_costs)
    
    for key in items:
      
        if key == "brown_bread":
            print("brown bread costs R%s "%(price_of_the_total_amount_of_brown_bread))
            
        if key == "brown_sugar":
            print("brown sugar costs R%s "%(price_of_the_total_amount_of_brown_sugar))
            
        if key == "soda":
            print("a soda costs R%s "%(price_of_the_total_amount_of_soda))
            
    calculate_price = price_of_the_total_amount_of_brown_bread + price_of_the_total_amount_of_brown_sugar + price_of_the_total_amount_of_soda
    print("total amount payed for the new stock R%s " %(calculate_price))
    

calculate_total_stock({"brown_bread":2,"brown_sugar":3,"soda":2})
calculate_price_new_stock({"brown_bread":2,"brown_sugar":3,"soda":2})
