from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')

elem = browser.find_element_by_css_selector('pass the selector')
elem.click() #clicks the specific selector

elems = browser.find_elements_by_css_selector('p') #finds the all paragraph items

#typing in the browser
searchElem = browser.find_elements_by_css_selector('.search-field')
searchElem.send_keys('zophie')
searchElem.submit()

browser.back()
browser.forward()
browser.refresh()
browser.quit()

# to read the content of webpage
elements = browser.find_elements_by_css_selector('selector')
elements.text
 