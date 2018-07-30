from selenium import webdriver
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
        self.assertIn('To-do', self.browser.title)
        self.fail('Finish the test!')

# He is prompted on the homepage to enter the first item on his to-do list

# He types "Solve a Codewars kata"

# When he hits enter, the page updates, and now the page lists
# "1: Solve a Codwewars kata" as an item in a to-do list

# There is still a text box inviting him to add another item. He enters
# "Mow and weedeat the lawn"

# The page updates again, and now shows both items on his list

# Philemon wonders whether the site will remember his list. Then he sees
# that the site has generated a unique URL for him -- there is some explanatory
# text to that effect

# He visits the URL - her to-do list is still there

# Satisfied, he goes back to sleep

if __name__ == '__main__':
    unittest.main()


