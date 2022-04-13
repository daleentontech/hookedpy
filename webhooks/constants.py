from decouple import config


# The webhook url will be provided to you by the recipient
# This is the url that will recieve and process the events that you will send out.
webhook_url = config("WEBHOOK_URL")