#!/usr/bin/env python
import unittest

def testnone(string):
    if type(string) == type(None):
       return True

def remove_spaces(string):
    if  testnone(string):
        return None
    if string[:1] == "":
       return ""
    elif string[:1] != " ":
       return string[:1] + remove_spaces(string[1:])
    else:
       return remove_spaces(string[1:])


def palindrome(string):
     if testnone(string):
        return False
     if string.__len__() <= 1: return True
     elif string[:1] == string[-1:] and\
           palindrome(string[2:-2]):
           return True
     else: return False

class test_remove_spaces (unittest.TestCase):
    def test_remove_space_none(self):
        self.assertEquals (remove_spaces (None), None)
    def test_remove_space_empty(self):
        self.assertEquals (remove_spaces (""), "")
    def test_remove_space_one(self):
        self.assertEquals (remove_spaces (" "), "")
    def test_remove_space_two(self):
        self.assertEquals (remove_spaces ("  "), "")
    def test_remove_space_inside(self):
        self.assertEquals (remove_spaces ("a b c"), "abc")
    def test_remove_space_before(self):
        self.assertEquals (remove_spaces (" a b c"), "abc")
    def test_remove_space_after(self):
        self.assertEquals (remove_spaces ("a b c "), "abc")
    def test_remove_space_before_and_after(self):
        self.assertEquals (remove_spaces (" a b c "), "abc")

    # this is extra credit
    # def test_raise_typerror(self):
        # self.assertRaises (TypeError, lambda: remove_spaces (1))

class test_palindrome (unittest.TestCase):
    def test_none(self):
        self.assertFalse (palindrome (None))
    def test_empty(self):
        self.assertTrue (palindrome (""))
    def test_one_letter(self):
        self.assertTrue (palindrome ("v"))
    def test_two_letters(self):
        self.assertTrue (palindrome ("vv"))
    def test_toyota(self):
        self.assertTrue (palindrome ("atoyota"))
    def test_toyota_with_spaces(self):
        self.assertTrue (palindrome (remove_spaces ("a toyota")))
    def test_odd_even(self):
        self.assertTrue (palindrome (remove_spaces ("never odd or even")))
    def test_rat(self):
        self.assertTrue (palindrome (remove_spaces ("Was It a Rat I saW")))
    def test_not(self):
        self.assertFalse (palindrome (remove_spaces ("i'm not a palindrome")))

if __name__ == '__main__':
    unittest.main()
