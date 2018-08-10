from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time


MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_for_one_user(self):
        # Philemon hears about a an online to-do app. He logs onto the web to check
        # out its homepage
        self.browser.get(self.live_server_url)

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
# When he hits enter, the page updates, and now the page lists
# "1: Solve a Codwewars kata" as an item in a to-do list
        inputbox.send_keys('Solve a Codewars kata')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Solve a Codewars kata')

# There is still a text box inviting him to add another item. He enters
# "Mow and weedeat the lawn"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Mow and weedeat the lawn')
        inputbox.send_keys(Keys.ENTER)

# The page updates again, and now shows both items on his list
        self.wait_for_row_in_list_table('1: Solve a Codewars kata')
        self.wait_for_row_in_list_table('2: Mow and weedeat the lawn')

# Philemon wonders whether the site will remember his list. Then he sees
# that the site has generated a unique URL for him -- there is some explanatory
# text to that effect
        self.fail('Finish the test!')

# He visits the URL - her to-do list is still there

# Satisfied, he goes back to sleep

    def test_multiple_users_can_start_lists_at_different_urls(self):
        #Philemon starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Solve a Codewars kata')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Solve a Codewars kata')

#He notices that his list has a unique url
        philemon_list_url = self.browser.current_url
        self.assertRegex(philemon_list_url, '/lists/.+')

#Now a new user, Francis, comes along to the site.

##We use a new browser session to make sure that no information
##of Philemon's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

        #Francis visit the home page. There is no sign of Philemon's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Solve a Codewars kata', page_text)
        self.assertNotIn('Mow and weedeat the lawn', page_text)

        #Franceis starts a new list by entering a new item.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        #Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, philemon_list_url)

        #Again, there is no trace of Philemon's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Sove a Codewars kata', page_text)
        self.AssertIn('Buy milk', page_text)

        #Satisfied, they both go back to sleep




