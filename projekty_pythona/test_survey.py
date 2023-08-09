import unittest

from survey import AnonymousSurvey

class TestAnonmyousSurvey(unittest.TestCase):
    """Testy dla klasy AnonymousSurvey"""
    
    def setUp(self):
        """Utworzenie ankiety i zestawu odpowiedzi do użycia we wszystkich metodach testowych."""
        question = "Jaki jest Twój ojczysty język?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['angielski','francuski','niemiecki']
    
    def test_store_single_reponse(self):
        """Sprawdzenie, czy pojedyncza odpowiedź jest odpowiednio przechowywana."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
        
    def test_store_three_responses(self):
        """Sprawdzenie, czy potrójna odpowiedź jest odpowiednio przechowywana."""    
        for response in self.responses:
            self.my_survey.store_response(response)
        
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()