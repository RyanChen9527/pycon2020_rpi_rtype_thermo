#-*- coding: utf-8 -*-　
import time
import urllib.request   #BI
from datetime import datetime   #BI

REST_API_URL = "https://api.powerbi.com/beta/ff0bcf0e-368a-4938-a92d-d84cb8180254/datasets/aa1bff63-b119-4a1d-9fcf-c2583ac4845e/rows?key=wWIC%2Bqmp2cP4kxO1kuvJBqijW8cH%2B60CKy1cnSb5MNhkqC3dBUlrghmj41e8oPIiypKoZ1vJgzamOge8U2tvgQ%3D%3D"

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

			
