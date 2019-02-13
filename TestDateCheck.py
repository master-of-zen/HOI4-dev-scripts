import unittest
import DateCheck
import settings


class TestDateCheck(unittest.TestCase):

    def test_cut_key(self):
        result = DateCheck.cut_key("			date > 1938.2.1")
        self.assertEqual(result, "1938.2.1")
        result = DateCheck.cut_key("			date > 1936.10.26 	#date = 1936.10.28")
        self.assertEqual(result, "1936.10.26")

    def test_line_is_valid(self):
        tc = DateCheck.line_is_valid("date > 1938.2.1", settings.date_key)
        self.assertEqual(True, tc )
        tc = DateCheck.line_is_valid("#date > 1938.2.1", settings.date_key)
        self.assertEqual(False, tc)



if __name__ == '__main__':
    unittest.main()



