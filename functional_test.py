from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Philemon hears about a an online to-do app. He logs onto the web to check
        # out its homepage
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

# He is prompted on the homepage to enter the first item on his to-do list
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

# He types "Solve a Codewars kata"
        inputbox.send_keys('Solve a Codewars kata')

# When he hits enter, the page updates, and now the page lists
# "1: Solve a Codwewars kata" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Solve a Codewars kata' for row in rows)
        )

# There is still a text box inviting him to add another item. He enters
# "Mow and weedeat the lawn"
        self.fail('Finish the test!')

# The page updates again, and now shows both items on his list

# Philemon wonders whether the site will remember his list. Then he sees
# that the site has generated a unique URL for him -- there is some explanatory
# text to that effect

# He visits the URL - her to-do list is still there

# Satisfied, he goes back to sleep

if __name__ == '__main__':
    unittest.main()


