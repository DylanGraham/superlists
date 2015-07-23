from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_list_and_retrieve(self):
        # User opens homepage
        self.browser.get('http://localhost:8000')

        # Page title mentions to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Can enter a to-do item right away
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )

        # Types 'Buy milk'
        inputbox.send_keys('Buy milk')

        # When enter pressed, the page updates and lists
        # '1: Buy milk' as an item on a to-do list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_id('tr')
        self.assertTrue(
                any(row.text == '1: Buy milk' for row in rows)
        )

        # Text box is offering to add another line.
        # User enters 'Bake cake'
        self.fail('Finish this test!')

        # The page updates and shows both items

        # The site has made a unique URL for the list
        # and lets the user know.

        # User goes to the URL, the list is there

if __name__ == '__main__':
    unittest.main()
