#!/usr/bin/env python
#############################
# Date: April 3rd, 2016
# Author: Sergiy Kolodyazhnyy
# Instructor: Steven Beaty
# Assignment: #4, Family Tree
# Description: Implementation of binary tree
# Tools used: vim, python 2.7
from __future__ import print_function
from sys import stdin
import unittest

'''Assignment:Add four different kinds of traversal to the following: 
   pre- in-, postorder, and breadth-first. 
   The "generations" method is where you need to do breadth-first. 
   Write unit tests as needed. '''

class family_tree:
    def __init__ (self, init = None):
        self.__value = self.__name = self.__parent = None
        self.__left = self.__right = None

        if init:
            try:
                for i in init:
                    self.add(i[0], i[1])
            except TypeError:
                self.add(init[0], init[0])

    def __iter__(self):
        if self.__left:
            for node in self.__left:
                yield(node)

        yield(self.__value, self.__name)

        if self.__right:
            for node in self.__right:
                yield(node)

    """ Return a preorder list """
    def preorder(self):
        nodes = ''
        nodes = '(' + str(self.__value) + ',' + self.__name + ')'
        if self.__left:
           nodes += ','
           nodes += self.__left.preorder()
        if self.__right:
           nodes += ','
           nodes += self.__right.preorder() 
        return nodes

    """ Return a inorder list """
    def inorder(self):
        nodes = ''
        if self.__left:
           nodes += self.__left.inorder() 
           nodes += ','
        nodes += '(' + str(self.__value) + ',' + self.__name + ')'
        if self.__right:
           nodes += ','
           nodes += self.__right.inorder() 
        return nodes


    """ Return a postorder list """
    def postorder(self):
        nodes = ''
        if self.__left:
           nodes += self.__left.postorder() 
           nodes += ','
        if self.__right:
           nodes += self.__right.postorder()
           nodes += ','
        nodes += '(' + str(self.__value) + ',' + self.__name + ')'
        return nodes


    def __str__(self): 
        return(','.join(str(node) for node in self))

    def add(self, value, name):
        if self.__value == self.__left == self.__right == None:
            self.__value = value
            self.__name = name
            self.__parent = None
            return

        if value < self.__value:
            if not self.__left:
                self.__left = family_tree()
                self.__left.__parent = self
                self.__left.__value = value
                self.__left.__name = name
            else:
                self.__left.add(value, name)
        else:
            if not self.__right:
                self.__right = family_tree()
                self.__right.__parent = self
                self.__right.__value = value
                self.__right.__name = name
            else:
                self.__right.add(value, name)
    
    """ Given a value, return the node with that value. Useful in the
    next two methods """
    def __find(self, value):
        if self.__value == value: return self

        if self.__value > value:
            if self.__left:
                return self.__left.__find(value)
            else:
                raise(LookupError)

        if self.__value < value:
            if self.__right:
                return self.__right.__find(value)
            else:
                raise(LookupError)

    """ Given a value, return the name of that node's parent """
    def find_parent(self, value):
        the_item = self.__find(value)
        if the_item.__parent:
           return the_item.__parent.__name
        else:
                raise(LookupError)
    """ Given a value, return the name of that node's grand parent """
    def find_grand_parent(self, value):
        the_item = self.__find(value)
        if the_item.__parent and the_item.__parent.__parent:
           return the_item.__parent.__parent.__name
        else:
                raise(LookupError)

    """ Create a list of lists, where each of the inner lists
        is a generation """
    def generations(self):
        # not implemented
         pass


class test_family_tree (unittest.TestCase):
    """
      20
     /  \
    10  30
       /  \
      25  35
    """
    def test_empty(self):
        self.assertEquals(str(family_tree()), '(None, None)')

    def setUp(self):
        self.tree = family_tree([(20, "Grandpa"), (10, "Herb"), \
        (30, "Homer"),(25, "Bart"), (35, "Lisa")])
        self.expected = "(10, 'Herb'),(20, 'Grandpa'),(25, 'Bart'),\
(30, 'Homer'),(35, 'Lisa')"

    def test_add(self):
        bt = family_tree()
        bt.add(20, "Grandpa")
        bt.add(10, "Herb")
        bt.add(30, "Homer")
        bt.add(25, "Bart")
        bt.add(35, "Lisa")
        self.assertEquals(str(bt), self.expected)

    def test_init(self):
        self.assertEquals(str(self.tree), self.expected)

    def test_parent(self):
        self.assertEquals(self.tree.find_parent(35), "Homer")

    def test_grand_parent(self):
        self.assertEquals(self.tree.find_grand_parent(35), "Grandpa")

    def test_pre_order(self):
        self.assertEquals( self.tree.preorder(),"(20,Grandpa),(10,Herb),(30,Homer),(25,Bart),(35,Lisa)"   )

    def test_in_order(self):
        self.assertEquals( self.tree.inorder(), "(10,Herb),(20,Grandpa),(25,Bart),(30,Homer),(35,Lisa)" )

    def test_post_order(self):
        self.assertEquals( self.tree.postorder(), "(10,Herb),(25,Bart),(35,Lisa),(30,Homer),(20,Grandpa)" )


    #def test_generations(self):
    #    self.assertEquals(self.tree.generations(), \
    #        [['Grandpa'], ['Herb', 'Homer'], ['Bart', 'Lisa']])




    """ Write your own tests for inorder etc. here """

if '__main__' == __name__:
    unittest.main()

    """ Read a file with lines of '# name'. Add each to a
    familty tree, and print out the resulting generations. """

    '''
    import sys
    ft = family_tree()
    with open(sys.argv[1]) as file:
     for line in file:   #stdin:
        a = line.strip().split(" ") # this splits into list of strings, but item 0 always is an int
        ft.add(int(a[0]), a[1]) # castig a[0] for consistency (  with unit tests and finder methods )
    #print(ft.generations())
    print("Parent of 35", ft.find_parent(35))
    print("Grandparent of 35",ft.find_grand_parent(35))
    print("Pre-order: ",ft.preorder())
    print("In-order: ",ft.inorder())
    print("Post-order: ",ft.postorder())
    '''
