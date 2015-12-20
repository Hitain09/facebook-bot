#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class FacebookStatus():

	def __init__(self):

		self.driver = webdriver.PhantomJS()											
		self.username = 'myFbName'			# user credentials
		self.passwd = passwd = 'myFbPassword'
		self.statusMessage = 'https://www.youtube.com/watch?v=D0BrG7O8wmA'

	# login facebook
	def loginFacebook(self):

		self.driver.get("https://www.facebook.com/")
		self.driver.find_element_by_id('email').clear()
		self.email = self.driver.find_element_by_id("email")
		self.email.send_keys(self.username)
		self.driver.find_element_by_id('pass').clear()
		self.password = self.driver.find_element_by_id("pass")
		self.password.send_keys(self.passwd)
		self.password.send_keys(Keys.RETURN)

	# status update fb user profile
	def statusProfile(self):

		self.driver.find_element_by_css_selector('.uiTextareaAutogrow.input.autofocus._34z-.mentionsTextarea.textInput').click()
		self.statusBox = self.driver.find_element_by_css_selector(".uiTextareaAutogrow.input.autofocus._34z-.mentionsTextarea.textInput")
		self.statusBox.send_keys(self.statusMessage)

		self.postButton = self.driver.find_element_by_css_selector('._42ft._4jy0._11b._4jy3._4jy1.selected._51sy')
		self.postButton.click()
		#self.driver.get_screenshot_as_file('/tmp/debug.png') 

	def quitDriver(self):
		self.driver.quit()

if __name__ == '__main__':

	updateStatus = FacebookStatus()
	updateStatus.loginFacebook()
	updateStatus.statusProfile()
	updateStatus.quitDriver()


