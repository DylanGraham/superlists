from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_list_and_retrieve(self):
        # User opens homepage
        self.browser.get(self.live_server_url)

        # Page title mentions to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Can enter a to-do item right away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Types 'Buy milk'
        inputbox.send_keys('Buy milk')

        # When enter pressed, the page updates and lists
        # '1: Buy milk' as an item on a to-do list
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: Buy milk')

        # Text box is offering to add another line.
        # User enters 'Bake cake'
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Bake cake')
        inputbox.send_keys(Keys.ENTER)

        # The page updates and shows both items
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Bake cake')

        # The site has made a unique URL for the list
        # and lets the user know.

        # User goes to the URL, the list is there
        self.fail('Finish this test!')
