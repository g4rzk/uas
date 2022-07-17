#!/usr/bin/python3
# user agent string
# made by angga kurniawan ! (@anggaxd)

import os
import sys
import json
import requests

ses = requests.Session()
class UAString:
	def __init__(self):
		self.url = "http://www.useragentstring.com"

	def __banner__(self):
		os.system("clear")
		print("             * - - == User Agent String == - - *")

	def __getUserAgent__(self):
		self.__banner__()
		get = input(" [?] input ua : ")
		if get in [""]:
			sys.exit("\n [!] jangan kosong coeg")
		else:
			try:
				data = ses.get(f"{self.url}?uas={get}&getJSON=all", headers={"user-agent": "Mozilla/5.0 (Linux; U; Android 7.1.2; en-us; Infinix X688B Build/NZH54D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.7.2"}).json()
			except:
				pass
		self.__getData__(data)

	def __getData__(self, data):
		print(f"\n [*] Agent Type : {data['agent_type']}")
		print(f" [*] Agent Name : {data['agent_name']}")
		print(f" [*] Agent Version : {data['agent_version']}")
		print(" [#] ----------------------------------------------")
		print(f" [*] OS Type : {data['os_type']}")
		print(f" [*] OS Name : {data['os_name']}")
		print(f" [*] OS Version Name : {data['os_versionName']}")
		print(f" [*] OS Version Number : {data['os_versionNumber']}")
		print(" [#] ----------------------------------------------")
		print(f" [*] Linux Distibution : {data['linux_distibution']}")
		print(f" [*] Agent Language : {data['agent_language']}")
		print(f" [*] Agent LanguageTag : {data['agent_languageTag']}")
		print(f"\n\n [+] API by {self.url}")

run = UAString()
run.__getUserAgent__()
