# TorCtl is depreciated...use Stem
from stem import Signal
from stem.control import Controller

def set_new_ip():
	# Change IP Using Tor
	with Controller.from_port(port = 9051) as controller:
		controller.authenticate()
		controller.signal(Signal.NEWNYM)