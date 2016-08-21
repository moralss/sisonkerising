import unittest
class Histogram:
    def draw(self,size):
        return '*'*size
    
    def draw_list(self,sizes):
        histogram = []
        for size in sizes:
            row = self.draw(size)
            histogram.append(row)
        return histogram
         
             
class Test_Histogram(unittest.TestCase):
    def draw_histogram(self,number):
        histo = Histogram()
        return histo.draw(number)
    
    def draw_histogram_list(self,numbers):
        histo_list = Histogram()
        return histo_list.draw_list(numbers)


    def test_given_3_then_draw_3_symbols(self):
        draw_value = self.draw_histogram(3)
        self.assertEqual(draw_value, "***")
        

    
    def test_given_list_then_draw_list_symbols2(self):
        sizes = [4,7]
        draw_histogram = self.draw_histogram_list(sizes)
        self.assertEqual(len(draw_histogram),len(sizes))




if __name__ == '__main__':
    unittest.main()



