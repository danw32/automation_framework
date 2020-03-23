# ** Daniel Whalley Jan 2020 ** #
import selenium_test_module
import unittest
import db_connection_module


class RunTestClass(unittest.TestCase):
    """Code for DB connection in db_connection_module.py"""

    def test_run_selenium_test(self):


        """loop through the rows in the DB rows"""
        print ("run the below...")
        ###works for one record - fetchone()
        #url_value = db_connection_module.record[0]
        #print (url_value)


        """works when there's cursor.fetchall() - in conn module"""
        second_row_tuple = db_connection_module.record[1]
        #print (second_row_tuple)
        url_value_second_row = second_row_tuple[0]
        print url_value_second_row


        """Instantiate selenium test class"""
        selenium_test_module_instance = selenium_test_module.SeleniumClass()

        """Runs the test to go to URLs in the spreadsheet test_sheet_YN.xls"""
        #selenium_test_module_instance.setUp()
        #selenium_test_module_instance.go_to_url(url_value)
        #selenium_test_module_instance.teardown()


if __name__ == "__main__":
    unittest.main()
