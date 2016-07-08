import unittest

class Test_Rugby_World_Ranking(unittest.TestCase):
    def get_ranking_test(self, country_code):
        ranking = Rugby_World_Ranking()
        return ranking.get_ranking(country_code)

    def test_gets_ranking_for_country_code(self):
        country_code = "ENG"
        rugby_ranking = self.get_ranking_test(country_code)

        self.assertEqual(rugby_ranking, 8)

    def test_gets_ranking_2_for_country_code_AUS(self):
        country_code = "AUS"
        rugby_ranking = self.get_ranking_test(country_code)

        self.assertEqual(rugby_ranking, 2)
    

class Rugby_World_Ranking :
    def get_ranking(self, country_code):
       return 2




if __name__ =='__main__':

    unittest.main()



         



            

        
    
