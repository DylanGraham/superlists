from selenium import webdriver

browser = webdriver.Firefox()

# User opens homepage
browser.get('http://localhost:8000')

# Page title mentions to-do lists
assert 'To-Do' in browser.title

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

browser.quit()
