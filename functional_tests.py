from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_list_and_retrieve(self):
        # User opens homepage
        self.browser.get('http://localhost:8000')

        # Page title mentions to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # Can enter a to-do item right away

        # Types 'Buy milk'

        # When enter pressed, the page updates and lists
        # '1: Buy milk' as an item on a to-do list

        # Text box is offering to add another line.
        # User enters 'Bake cake'

        # The page updates and shows both items

        # The site has made a unique URL for the list
        # and lets the user know.

        # User goes to the URL, the list is there

if __name__ == '__main__':
    unittest.main(warnings='ignore')

