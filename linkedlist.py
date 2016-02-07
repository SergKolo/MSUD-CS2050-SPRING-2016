#!/usr/bin/env python
#############################
# Date: February,6th,2016
# Author: Sergiy Kolodyazhnyy
# Instructor: Steven Beaty
# Assignment: #1, Linked List
# Description: Implementation of stack
# using singly linked list ,which itself is
# implemented as an object
# Tools used: vim, python 2.7
import unittest


class test_linked_list (unittest.TestCase):
    def test_none(self):
        self.assertTrue(linked_list().empty())
    def test_pop_front_empty(self):
        self.assertRaises(RuntimeError, lambda: linked_list().pop_front())
    def test_pop_back_empty(self):
        self.assertRaises(RuntimeError, lambda: linked_list().pop_back())
    def test_push_back_pop_front(self):
        ll = linked_list()
        ll.push_back(1)
        ll.push_back(2)
        ll.push_back(3)
        self.assertFalse(ll.empty())
        self.assertEquals(ll.pop_front(), 1)
        self.assertEquals(ll.pop_front(), 2)
        self.assertEquals(ll.pop_front(), 3)
        self.assertTrue(ll.empty())
    def test_push_front_pop_front(self):
        ll = linked_list()
        ll.push_front(1)
        ll.push_front(2)
        ll.push_front(3)
        self.assertEquals(ll.pop_front(), 3)
        self.assertEquals(ll.pop_front(), 2)
        self.assertEquals(ll.pop_front(), 1)
        self.assertTrue(ll.empty())
    def test_push_front_pop_back(self):
        ll = linked_list()
        ll.push_front(1)
        ll.push_front(2)
        ll.push_front(3)
        self.assertFalse(ll.empty())
        self.assertEquals(ll.pop_back(), 1)
        self.assertEquals(ll.pop_back(), 2)
        self.assertEquals(ll.pop_back(), 3)
        self.assertTrue(ll.empty())
    def test_push_back_pop_back(self):
        ll = linked_list()
        ll.push_back(1)
        ll.push_back("foo")
        ll.push_back([3,2,1])
        self.assertFalse(ll.empty())
        self.assertEquals(ll.pop_back(),[3,2,1])
        self.assertEquals(ll.pop_back(), "foo")
        self.assertEquals(ll.pop_back(), 1)
        self.assertTrue(ll.empty())

class linked_list:
  def __init__(self):
       self.front = self.rear = None 

  class node:
        def __init__(self,data,next):
            self.data = data
            self.next = next


  def empty(self): 
      if self.rear == None:
          return True


  def push_front(self,data):
      newNode = self.node(data,self.front)
      self.front = newNode
      if not self.rear :
         self.rear = newNode
         
  def pop_front(self):
         if self.empty():
            raise RuntimeError("List is empty,nothing to remove")
         popped = self.front.data
         if self.front == self.rear:
            self.rear = None
         else:
            self.front = self.front.next
         return popped


  def push_back(self,data):
      newNode = self.node(data,None)
      if not self.rear:
           self.front = self.rear = newNode
      else:
           penultimate = self.rear
           penultimate.next = newNode
           self.rear = newNode
 
  def pop_back(self):
      if self.empty():
         raise RuntimeError("List is empty,nothing to remove!")
      popped = self.rear.data
      penultimate = self.front
      if self.rear == self.front:
            self.rear = self.front = None
      else:
           while penultimate.next.next :
                  penultimate = penultimate.next
           self.rear = penultimate
           penultimate.next = None
      return popped
            
      
      
      
  def peek(self):
      if not self.empty():
             print self.front.data   
    
          
class factorial:
  def fact(self,a):
    if a < 0: raise ValueError("Less than zero")
    if a == 0 or a == 1 : return 1
    stack = linked_list()
    while a > 1:
      stack.push_back(a)
      a -= 1
    result = 1
    while not stack.empty():
       popped = stack.pop_back()
       result *= popped
    return result   

class test_factorial (unittest.TestCase):
    def test_less_than_zero(self):
        self.assertRaises(ValueError, lambda: factorial().fact(-1))
    def test_zero(self):
        self.assertEquals(factorial().fact(0), 1)
    def test_one(self):
        self.assertEquals(factorial().fact(1), 1)
    def test_two(self):
        self.assertEquals(factorial().fact(2), 2)
    def test_10(self):
        self.assertEquals(factorial().fact(10), 10*9*8*7*6*5*4*3*2*1)

if __name__ == '__main__': 
#   unittest.main()

   print factorial().fact(1)
   print factorial().fact(5)
   print factorial().fact(100)
