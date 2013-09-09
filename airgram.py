from urllib import urlencode
from base64 import encodestring
import urllib2

# A wrapper around the Airgram API, http://www.airgramapp.com/.
# author: varun
# author: Sidhant Gupta - authentication and defs for airgram service 


class Airgram(object):
	"""Wrapper around the Airgram API."""

	BASE_URL = "https://api.airgramapp.com/1"
	KEY = None
	SECRET = None

	def __init__(self, key=None, secret=None):
		self.KEY = key
		self.SECRET = secret

	def check_auth(self):
		if self.KEY is None or self.SECRET is None:
			raise Exception('Attempt to use function that requires a service key and secret!')

	def send(self, email, msg, url=None):
		"""Send a push notification to specified user"""

		self.check_auth()

		params = {
		"email": email,
		"msg": msg,
		}
		if (url):
			params["url"] = url
		return self._post("/send", params, True)

	def subscribe(self, email):
		"""Subscribe a new user to service"""

		self.check_auth()
		params = {"email": email}
		return self._post("/subscribe", params, True)

	def broadcast(self, msg, url=None):
		"""Send a push notification to all subscribed users"""

		self.check_auth()

		params = {"msg": msg}
		if (url):
			params["url"] = url
		return self._post("/broadcast", params, True)

	def send_as_guest(self, email, msg, url=None):
		"""Send a push notification as a guest. No need to register your service.

		Args:
			email: The email to which you want to send the notification.
			msg: The notification msg.
			url: If the notification should direct you to a url.

		Returns:
			The response content.
		"""
		params = {
				"email": email,
				"msg": msg,
		}
		if (url):
			params["url"] = url
		return self._post("/send_as_guest", params)

	def _post(self, path, decoded_params, auth=None):
		url = "%s%s" % (self.BASE_URL, path)
		params = urlencode(decoded_params)
		req = urllib2.Request(url, params)
		
		if (auth):
			base64string = encodestring('%s:%s' % (self.KEY, self.SECRET)).replace('\n', '')
			req.add_header("Authorization", "Basic %s" % base64string)  
		
		rsp = urllib2.urlopen(req)
		content = rsp.read()
		return content
