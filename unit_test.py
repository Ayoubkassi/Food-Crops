from test import find
import unittest



class TestFilter(unittest.TestCase):
    def test_filter(self):
	    self.assertEqual(find(None,18,None)[1].name,"Ayoub")

if __name__ == "__main__":
    unittest.main()