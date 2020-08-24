import unittest
import sys
# Is there another way to import from different folder without using folder path?
sys.path.insert(1, "C:/Users/Kyle/Desktop/CODE/Python/AutoGrader/src")
from docScan import docToText, textToAnswers, numberedTextToAnswers, grader

class TextTestCase(unittest.TestCase):
    # every text file should be parsed to be the same as 'answers'
    # all dots in answers should've been converted to +
    answers = {"1": "A", "2": "B", "3": "C", "4": "D", "5": "A", "6": "B", "7": "12", "8": "0+25", "9": "9/4", "10": "3+14"}

    # need to start with 'test'!!
    def test_dot(self):
        file = docToText("testfiles/neatDot.txt")
        read = numberedTextToAnswers(file)
        self.assertEqual(read, TextTestCase.answers)
    
    def test_space(self):
        file = docToText("testfiles/neatSpace.txt")
        read = numberedTextToAnswers(file)
        self.assertEqual(read, TextTestCase.answers)
    
    def test_dash(self):
        file = docToText("testfiles/neatDash.txt")
        read = numberedTextToAnswers(file)
        self.assertEqual(read, TextTestCase.answers)
    
    def test_parenthesis(self):
        file = docToText("testfiles/neatParen.txt")
        read = numberedTextToAnswers(file)
        self.assertEqual(read, TextTestCase.answers)

    def test_mixed(self):
        file = docToText("testfiles/neatMixed.txt")
        read = numberedTextToAnswers(file)
        self.assertEqual(read, TextTestCase.answers)    

    def test_messy(self):
        file = docToText("testfiles/messy.txt")
        read = numberedTextToAnswers(file)
        self.assertEqual(read, TextTestCase.answers)        





if __name__=="__main__":
    unittest.main()

