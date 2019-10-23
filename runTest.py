# ** Daniel Whalley August 2019 ** #
import selenium_test_module
from read_sheet import *
import unittest
from helper_module import *


class RunTestClass(unittest.TestCase):
    """Change the spreadsheet to use in readsheet.py"""

    def test_run_selenium_test(self):


        """loop through the rows in the spreadsheet"""
        for i in range(len(data)):

            if data[i]['Run'].lower() == 'y':
                print ("run the below...")
                url_value = data[i]['URL']
                password_value = data[i]['password']
                username_value = data[i]['username']

                """Uncomment these when running Ladbrokes lottery test"""
                # first_number_int = int(data[i]['first_number'])
                # second_number_int = int(data[i]['second_number'])
                # first_number_value = str(first_number_int)
                # second_number_value = str(second_number_int)

                print (url_value)
                print (password_value)
                print (username_value)
                # print (first_number_value)
                # print (second_number_value)

                """Instantiate selenium test class"""
                selenium_test_module_instance = selenium_test_module.SeleniumClass()

                """Runs the Ladbrokes lottery test in the spreadsheet ladbrokes_sheet.xls"""
                # selenium_test_module_instance.test_selenium_code_lottery(url_value, username_value, password_value, first_number_value, second_number_value)

                """Runs the test to go to URLs in the spreadsheet test_sheet_YN.xls"""
                selenium_test_module_instance.setUp()
                selenium_test_module_instance.go_to_url(url_value)
                selenium_test_module_instance.teardown()

                """Clean up screenshots. Move the files to relevant folders in Screenshots directory"""
                move_png(i + 1)


            elif data[i]['Run'].lower() == 'n':
                print ("Don't run row " + str(i + 1))
                # tkMessageBox.showinfo("Information", "'" + Name_of_site + "'" + " not run")
            elif data[i]['Run'].lower() != 'n' or data[i]['Run'].lower() != 'y':
                print ("enter something useful: Y or N")
            else:
                pass



if __name__ == "__main__":
    unittest.main()
