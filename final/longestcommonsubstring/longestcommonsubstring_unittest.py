#!/usr/bin/env python3
import unittest
from longestcommonsubstring import long_substr

class LongestCommonSubstringTest(unittest.TestCase):        
    def test_two_equal_words(self):
        word_list = ['test', 'test']
        resulting_substring = long_substr(word_list)
        self.assertEqual(resulting_substring, 'test', "The words are the same, so they have the same common substring.")
        self.assertEqual(len(resulting_substring), 4, "The words are the same, so they have the same common substring.")
    
    def test_one_empty_word(self):
        word_list = ['test', '']
        resulting_substring = long_substr(word_list)
        self.assertEqual(resulting_substring, '', "The second word doesn't have any characters, so there is no common substring.")
        self.assertEqual(len(resulting_substring), 0, "The second word doesn't have any characters, so there is no common substring.")
        
    def test_two_empty_words(self):
        word_list = ['', '']
        resulting_substring = long_substr(word_list)
        self.assertEqual(resulting_substring, '', "Neither word has any characters, so there is no common substring.")
        self.assertEqual(len(resulting_substring), 0, "Neither word has any characters, so there is no common substring.")
    
    
    def test_many_words(self):
        word_list = ['abcdefghijklmnopqrstuvwxyz', 'efk', 'bcefdafzka']
        resulting_substring = long_substr(word_list)
        self.assertEqual(resulting_substring, 'ef', "They all share two letters in a row.")
        self.assertEqual(len(resulting_substring), 2, "They all share two letters in a row.")
   
        
if __name__ == "__main__":
    unittest.main(verbosity=2)
