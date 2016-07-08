import unittest

current_stock = [{"name_of_stock":"brown_bread","quantity":3,"price":1},
                 {"name_of_stock":"brown_sugar","quantity":2,"price":5}
                 ]
                 
def calculate_total_stock(new_stock):
     for new_stock_key in new_stock:
         for current_stock_key in current_stock:
              total = new_stock_key["quantity"] + current_stock_key["quantity"]
              print(total)
              
            
def add_new_stock(new_stock):
    for new_stock_item in new_stock:
        found = False
        for current_stock_item in current_stock:
            if current_stock_item["name_of_stock"] == new_stock_item["name_of_stock"]:
                  current_stock_item["quantity"] = current_stock_item["quantity"] + new_stock_item["quantity"]
                  found = True
                  continue
    if not found:
        current_stock.append(new_stock_item)
     

add_new_stock([{"name_of_stock":"brown_bread","quantity":2,"price":1},
                       {"name_of_stock":"brown_sugar","quantity":5,"price":5},
                         {"name_of_stock":"white_sugar","quantity":5,"price":3}])



class StockTests(unittest.TestCase):
    def test_we_can_update_stock_of_current_stock_items(self):
        #given
        stock_item_to_add = {"name_of_stock":"brown_bread","quantity":2,"price":1}

        #when
        add_new_stock([stock_item_to_add])

        #then
        brown_bread_stock_item = next(filter(lambda stock_item: stock_item["name_of_stock"] == "brown_bread", current_stock))
        self.assertEqual(brown_bread_stock_item["quantity"], 7)

if __name__ =='__main__':

    unittest.main()