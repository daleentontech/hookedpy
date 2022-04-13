# hookedpy

Send and Receive Webhooks with Django (Reference)

# Receiving Webhooks

## Using [Ngrok](https://www.ngrok.com)

1. setup ngrok on your machine
2. tunnel your port to ngrok to make it publicly available (put your local host on the internet)

```bash
./ngrok http 8000
```

3. ngrok will then provide a publicly available url that fowards to your localhost(reverse proxy)

`http://83d4-169-255-125-200.ngrok.io -> http://localhost:8000`

#### Process The Event

You are now ready to process webhook events

- Provide your webhook URL `http://83d4-169-255-125-200.ngrok.io/hook/process/` to whoever will be sending you webhooks
- The logic on /hook/process should then parse the event and do with it as you have commanded.

# Sending Webhooks

Sending webhook events is pretty much straightfoward.

1. Receive the destination webhook URL
2. get the data ready
3. call the `http://localhost:8000/hook/send/` endpoint with the data

```curl
curl -X POST http://localhost:8000/hook/send/ -d '{"foo": "bar"}'
```
