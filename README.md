airgram
=======

A wrapper for the Airgram API.
http://www.airgramapp.com/

This wrapper lets you conveniently use the Airgram API from python to send push notification to a phone.

###USAGE
The Airgram object can either be initialized with a key and secret for your Airgram service or be left out to use the IP rate-limited guest mode. See [AirGram Docs](http://www.airgramapp.com/docs) for details.

```python
import airgram

# Guest mode
ag = airgram.Airgram()

# Send message with an optional url
ag.send_as_guest("user@email.com", "Hello, World!", "http://www.example.com")

# Push notification using custom Airgram service - *requires* service key and secret
ag = airgram.Airgram(key="XXXX", secret="XXXX"))

# Subscribe a new user
ag.subscribe("new_user@example.com")

# Send message to a subscribed user with an optional url
ag.send("user@example.com", "Hello, World!", "http://www.example.com")

# Broadcast message to *all* subscribed users
ag.broadcast("This is an announcement")
```