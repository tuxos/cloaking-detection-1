import hashlib
import sys
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sets import Set
from util import start_browser

def hex_md5(string):
	# util function to return md5 in hex of the input string.
	m = hashlib.md5()
	m.update(string.encode('utf-8'))
	return m.hexdigest()

def mkdir_if_not_exist(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)

class Crawler:
	# 1. Because we are working on visiting URLs or ad clickstrings (from Google ads), assume we don't need the referer file.
	# 2. If we really need referer, one way is to directly do crawling from hot search words.
	def __init__(self, url_file, user_agent_file, threads=10):
		# Prepare the output directory
		now = datetime.now().strftime("%Y%m%d-%H%M%S")
		self.base_dir = url_file + '.' + now + '.selenium.crawl/'
		mkdir_if_not_exist(self.base_dir)
		# Prepare the input
		self.urls = filter(bool, open(url_file, 'r').read().split('\n'))
		self.user_agents = filter(bool, open(user_agent_file, 'r').read().split('\n'))
		# self.referers = filter(bool, open(referer_file, 'r').read().split('\n'))
		self.threads = threads

		# Prepare log files
		self.htmls_f = open(self.base_dir + 'html_path_list', 'a')
		self.md5_UA_f = open(self.base_dir + 'md5_UA.log', 'a')  # user agent
	
	def new_session(self, user_agent, threads):
		user_agent_md5 = hex_md5(user_agent)
		user_agent_md5_dir = self.base_dir + user_agent_md5 + '/'
		mkdir_if_not_exist(user_agent_md5_dir)

		# md5 - user agent mapping logs
		self.md5_UA_f.write(use_agent_md5 + ":" + user_agent + "\n")

		# the user could create multiple sessions
		# for each session, the program can be threaded
		if 'Chrome' in user_agent:
			browser_type = 'Chrome'
		elif 'Firefox' in user_agent:
			browser_type = 'Firefox'
		elif 'bot' in user_agent:
			browser_type = 'Firefox'
		else:
			browser_type = 'Firefox'
		browser = start_browser(browser_type, incognito=False, user_agent=user_agent)

		# url md5 - landing url logs
		url_md5_LP_f = open(user_agent_md5_dir + 'landing_page', 'r')
		success_f = open(user_agent_md5_dir + 'success', 'r')
		failure_f = open(user_agent_md5_dir + 'failure', 'r')

		for url in self.urls:
			browser.get(url)
			# if url loading failed!
			#############
			# md5 the original url
			url_md5 = hex_md5(url)
			url_md5_dir = user_agent_md5_dir + url_md5 + '/'
			mkdir_if_not_exist(url_md5_dir)
			# get the landing url
			landing_url = browser.current_url
			landing_url_md5 = hex_md5(landing_url)
			# get the whole page source
			response = browser.execute_script("return document.documentElement.innerHTML;")
			response_filename = url_md5_dir + 'index.html'
			f = open(response_filename, 'w')
			f.write(response.encode('utf-8'))
			f.close()

			# md5 - landing page mapping logs
			url_md5_LP_f.write(url_md5 + ':' + landing_url + '\n')
			log_str = url_md5 + ':' + url + ':' + landing_url_md5 + ':' + landing_url + '\n'
			if success:
				success_f.write(log_str)
			else:
				failure_f.write(log_str)

def main(argv):
	print len(argv)
	"""
	crawler = Crawler('', '', '')
	crawler.new_session('', 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X; en-us) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53', '', 10)
	crawler.new_session('', 'Mozilla/5.0 (Linux; <Android Version>; <Build Tag etc.>) AppleWebKit/<WebKit Rev> (KHTML, like Gecko) Chrome/<Chrome Rev> Mobile Safari/<WebKit Rev>', '', 10)
	"""
	crawler = Crawler(argv[0], argv[1])
	for user_agent in crawler.user_agents:
		crawler.new_session(user_agent, 10)

if __name__ == "__main__":
	main(sys.argv[1:])


