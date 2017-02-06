# TorCtl is depreciated...use Stem
from stem import Signal
import requests
from stem.control import Controller

def set_new_ip():
	# Change IP Using Tor
	with Controller.from_port(port = 9051) as controller:
		controller.authenticate()
		controller.signal(Signal.NEWNYM)

def gather_reqs():
	local_proxy = '127.0.0.1:8118'
	http_proxy = {'http' : local_proxy, 'https' : local_proxy}

	current_ip = requests.get(url = 'http://icanhazip.com/', proxies = http_proxy, verify = False)