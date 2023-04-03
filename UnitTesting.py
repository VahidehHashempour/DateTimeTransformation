#Unit Testing
import unittest
from datetime import datetime

class TestGetDateTime(unittest.TestCase):
    # Check to see if the return value of current_date_time() is the same as current system time
    def test_date(self):
        self.assertEqual(current_date_time(), datetime.now())
        
        
class TestDateTimeFormat(unittest.TestCase): 
  
    # Check to see if the return value of datetime_string_1() is in the form of "%d/%m/%Y %A %H:%M:%S"
    def test_date_format1(self):
        self.assertEqual(datetime_string_1(datetime.now()), datetime.now().strftime("%d/%m/%Y %A %H:%M:%S"))
    
    # Check to see if the return value of datetime_string_1() is in the form of "%d-%m-%Y %A %H:%M:%S"
    def test_date_format2(self):
        self.assertEqual(datetime_string_2(datetime.now()), datetime.now().strftime("%d-%m-%Y %A %H:%M:%S"))
    
    # Check to see if the return value of datetime_string_1() is in the form of "%d/%m/%Y %A %I:%M:%S %p"
    def test_date_format3(self):
        self.assertEqual(datetime_string_3(datetime.now()), datetime.now().strftime("%d/%m/%Y %A %I:%M:%S %p"))
    
    # Check to see if the return value of datetime_string_1() is in the form of "%d-%m-%Y %A %I:%M:%S %p"
    def test_date_format4(self):
        self.assertEqual(datetime_string_4(datetime.now()), datetime.now().strftime("%d-%m-%Y %A %I:%M:%S %p"))    

if __name__ == '__main__':
    unittest.main()
