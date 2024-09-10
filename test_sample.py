import sample
import unittest


# Unit test class
class TestFunctions(unittest.TestCase):

    def test_print(self):
        # Test the print function
        result = sample.printt()
        self.assertEqual(result, "function #DEF")

    def test_write(self):
        # Test the write function with sample input
        result = sample.write("this is written")
        self.assertEqual(result, "write this is written ")

# This allows the test to run when the script is executed
if __name__ == '__main__':
    unittest.main()
