import unittest
import DateCheck


class TestDateCheck(unittest.TestCase):

    def test_cut_key(self):
        result = DateCheck.cut_key("			date > 1938.2.1")
        self.assertTrue(result, "1938.2.1")
        result = DateCheck.cut_key("			date > 1936.10.26 	#date = 1936.10.28")
        self.assertTrue(())

if __name__ == '__main__':
    unittest.main()