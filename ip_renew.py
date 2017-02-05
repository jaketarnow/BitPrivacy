# Implemented from http://sacharya.com/crawling-anonymously-with-tor-in-python/
from TorCtl import TorCtl
import urllib2

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0'
headers = {'User-Agent':user_agent}

def request(url):
	def _set_urlproxy():
		proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:8118"})
		opener = urllib2.build_opener(proxy_support)
	_set_urlproxy()
	request = urllib2.Request(url, None, headers)
	return urllib2.urlopen(request).read()

def renew_connection():
	conn = TorCtl.connect(controlAddr = "127.0.0.1", controlPort = 9050, passphrase = "")
	conn.send_signal("NEWNYM")
	conn.close()

for i in range(0, 10):
	renew_connection()
	print request("https://blockchain.info/")
	