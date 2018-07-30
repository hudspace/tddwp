from selenium import webdriver

path="/usr/local/bin/geckodriver"
browser = webdriver.Firefox(executable_path=path)
browser.get('http://localhost:8000')

assert 'Django' in browser.title
