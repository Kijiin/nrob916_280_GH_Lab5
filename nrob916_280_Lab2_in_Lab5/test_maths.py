import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function. '''
        first = 3
        second = 6
        n = 10
        self.assertEqual(maths.add(first, second, n), first + second, n)
        
        pass # TODO
    
    def test_add_base(self):
        b = maths
        n=10
        b.add(3, 6, n)
        
        self.assertTrue(n>0 and n<11)
        
        pass
    def test_add_base_over_10(self):
        b = maths
        n = 12
        b.add(3,6, n)
        
        self.assertTrue(n>10)
        
        pass   
    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        length = 5
        
        self.assertEqual(maths.fibonacci(length), length)
        
        pass # TODO
    
    def test_convert_base_under_10(self):
        b = maths
        n=9
        b.convert_base(20,n)
        
        self.assertTrue(n>0 and n<10)
        
        pass
        
    def test_convert_base_over_10(self):
        b = maths
        n = 12
        b.convert_base(20,n)
        
        self.assertTrue(n>10)
        
        pass

    def test_factorial(self):
        b = maths
        n = 3
        self.assertEqual(b.factorial(n), 6)
# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
