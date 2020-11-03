#Step 1 − Import the unittest module in your program.
import unittest
from serializetopicle import serialize_to_pickle as ser #uses adding.py code from module you're testing
from K9 import __Dog # Dog class from K9.py
#Step 2 − Define a function to be tested. 
# In the following example, add() function is to be subjected to test.
obj=object()
#xobj = object()
obj = __Dog(1,"Rex",1) 
xstr = 'serialized_obj'
print("Dog number is: ",obj.number," Dog name is : ",obj.name," Dog age is: ",obj.age)
#def add(x, y):
#   return x + y
# Step 3 − Create a testcase by subclassing unittest.TestCase.
class SimpleTest(unittest.TestCase):
   # Step 4 − Define a test as a method inside the class.
   #  Name of method must start with 'test'.
   def test_obj_to_pickle_file(self):
      """test case A"""
      # Step 6 − assertEquals() function compares
      #  result of add() function with arg2 argument
      #  and throws assertionError if comparison fails.
      #
      #uses adding.py
      self.assertIsInstance(ser.obj_to_pickle_file(self,obj,xstr), type(obj))
   
   #unittest
   def test_add_B(self):
      """test case B"""
      # Step 6 − assertEquals() function compares
      #  result of add() function with arg2 argument
      #  and throws assertionError if comparison fails.
      #
      #uses adding.py
      self.assertEqual(obj.name,"Rex",None)
         
   def test_add_C(self):
      """test case B"""
      # Step 6 − assertEquals() function compares
      #  result of add() function with arg2 argument
      #  and throws assertionError if comparison fails.
      #
      #uses adding.py
      def obj_from_pickle(self,obj:object,xstr:str):
          self.assertNotEqual(obj.age,2)
   #   
   
# Step 7 − Finally, call main() method from the unittest module.
if __name__ == '__main__':
   unittest.main()