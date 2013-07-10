import urllib, urllib2

# A wrapper around the Airgram API, http://www.airgramapp.com/.
# author: varun

class Airgram(object):
  """Wrapper around the Airgram API."""

  BASE_URL = "https://api.airgramapp.com/1"

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
    params = urllib.urlencode(decoded_params)
    req = urllib2.Request(url, params)
    rsp = urllib2.urlopen(req)
    content = rsp.read()
    return content
