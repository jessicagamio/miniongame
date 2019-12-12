import unittest


def minion_game(string):

    string = string.lower()

    vowels = 'aeiou'

    kevin_points = 0 #vowel 
    stuart_points = 0 # consonant 


    # add the length of string[i:] at every occurance of vowel in string
    for i, ltr in enumerate(string):
        if string[i] in vowels:
            kevin_points += len(string) - i

        else:
            stuart_points += len(string) - i 
 

    if kevin_points == stuart_points:
        return "Draw"

    elif kevin_points > stuart_points:
        return f"Kevin {kevin_points}"

    else:
        return f"Stuart {stuart_points}"

   
            
class TestFucntion(unittest.TestCase):
    def testMethod(self):
        self.assertEqual(minion_game("banana"), "Stuart 12")
 
        self.assertEqual(minion_game("ANANAS"),"Kevin 12")


if __name__ == "__main__":
    unittest.main()

