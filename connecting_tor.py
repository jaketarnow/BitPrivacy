import stem.process
import stem.connection
import stem.socket
from stem import Signal
from stem.control import Controller
from splinter import Browser

proxyIP = "127.0.0.1"
proxyPort = 9050
#http://www.thedurkweb.com/automated-anonymous-interactions-with-websites-using-python-and-tor/
browser = Browser('firefox')

def switchIP():
	with Controller.from_port(port=proxyPort) as controller:
		controller.authenticate()
		bytes_read = controller.get_info("traffic/read")
		bytes_written = controller.get_info("traffic/written")
		print("My Tor relay has read %s bytes and written %s." % (bytes_read, bytes_written))
		#controller.signal(Signal.NEWNYM)
		# NEWNYM used to send to Tor connection

for x in range(50):
	browser.visit("https://check.torproject.org/")
	switchIP()
	time.sleep(5)