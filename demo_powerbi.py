#-*- coding: utf-8 -*-　
import time
import urllib.request   #BI
from datetime import datetime   #BI

REST_API_URL = "ENTER_YOUR_API_KEY_HERE"

def upload_powebi(temp):
		now = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S%Z")
		data = '[{{ "timestamp": "{0}", "temperature": "{1}" }}]'.format(now, temp)
		data=data.encode("utf-8")
		try:
			req=urllib.request.Request(REST_API_URL, data)
			urllib.request.urlopen(req)
			print("upload_success") 
		except Exception as info:
			print('update_trouble=>'+str(info))

if __name__ == "__main__":
	while True:
			upload_powebi(18)
			time.sleep(3)

			
